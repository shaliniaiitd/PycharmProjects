import uuid
from datetime import datetime
from typing import Text

from pyspark.shell import spark
from pyspark.sql import SparkSession

from we.pipeline.core.util.configuration_util import to_database_name
from we.pipeline.validation.task.validation_context import ValidationContext


class Validation_C:
    def validate(self):
        """Validate some test results.
        :return: True if all expectations are met. False if some expectations are not met.
        """

        return True


class SpaceValidation(Validation_C):
    def __init__(self,
                 spark: SparkSession,
                 run_id: Text,
                 use_case_id: Text,
                 validation_context: ValidationContext):
        self.spark = spark
        self.run_id = run_id
        self.use_case_id = use_case_id
        self.validation_context = validation_context

    def validate_space(self):
        date_time_obj = datetime.utcnow()
        batch_id = self.use_case_id
        current_timestamp_val = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        job_log_key = str(uuid.uuid4())
        ctx = self.validation_context
        pipeline = ctx.pipeline
        object_type = ctx.object_type
        zone = ctx.zone
        target_tablename = ctx.target_tablename
        validation_type = "space_check"
        target_database = to_database_name(ctx.space, ctx.target_zone, ctx.data_group)
        # To describe the table
        df_source_schema = spark.sql(f"""desc {ctx.catalog_name}.{target_database}.{ctx.target_tablename}""")
        df_source_schema.createOrReplaceTempView("source_schema_temp_view")
        # To get and collect all columns of the table
        select_col_name = spark.sql("""select col_name from source_schema_temp_view""")
        select_col_name.createOrReplaceTempView("col_name_temp_view")
        # Convert column captured into a list
        col_list = [list(row) for row in select_col_name.collect()]

        # Captured number of items in the list
        length = len(col_list)
        # To select all value of the table
        select_all = spark.sql(f"""select * from {ctx.catalog_name}.{target_database}.{ctx.target_tablename}""")
        select_all.createOrReplaceTempView("select_all_temp_view")
        # # Drop space validation table
        # spark.sql(f"""DROP TABLE {ctx.catalog_name}.{target_database}.{ctx.pipeline}_{ctx.object_type}_space_validation""")

        for row in range(length):
            listing = col_list[row]

            # To convert the column from list to string
            col_string = ', '.join(str(item) for item in listing)

            '''df_space_validation = spark.sql(f"""
                 select * from
                 (
                     select *,
                     rtrim(ltrim('{col_string}')) as data_with_spaces,
                     case when '{col_string}' not like rtrim(ltrim('{col_string}')) then
                         'Have Space'
                     else
                         'None'
                     end as space_flag
                     from select_all_temp_view
                 )
                 where space_flag = 'Have Space'
             """)'''

            df_space_validation = spark.sql(
                f"""
                             select
                             '{batch_id}' as batch_id,
                             '{pipeline}' as pipeline_type,
                             '{object_type}' as object_type,
                             '{validation_type}' as validation_type,
                             '{zone}' as zone,
                             cast('NA' as string) as source_location,
                             cast('NA' as string) as source_database,
                             cast('NA' as string) as source_tablename,
                             '{target_database}' as target_database,
                             '{target_tablename}' as target_tablename,
                             '{col_string}' as target_column,
                             null as source_row_count,
                             count(*) as target_row_count,
                             count(case space_flag when 'None' then 1 else null end) as success_count,
                             count(case space_flag when 'Have Space' then 1 else null end) as failure_count,
                             (
                                 case
                                 when count(case space_flag when 'Have Space' then 1 else null end) = 0 then 'No Leading and Trailing space found for "{col_string}"'
                                 else 'Leading and Trailing space found for "{col_string}"'
                                 end
                             ) as validation_status,
                             '{current_timestamp_val}' as record_created_timestamp,
                             '{job_log_key}' as job_log_key
                             from
                             (
                                 select
                                 rtrim(ltrim({col_string})) as data_with_spaces,
                                 (case when {col_string} not like rtrim(ltrim(translate({col_string},'\\',''))) then 'Have Space' else 'None' end) as space_flag
                                 from
                                 {ctx.catalog_name}.{target_database}.{target_tablename}
                             )
                         """
            )

            df_space_validation.createOrReplaceTempView("space_validation_temp_view")

            #validation_table = "altrata_data_lake_test.synthetic_silver_dd.pipeline_validation_report"
            #validation_table = f"{ctx.catalog_name}.{ctx.space}.{ctx.pipeline}_validation_report"
            db_name = f"{ctx.catalog_name}.{ctx.space}_validation_database"
            spark.sql(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            validation_table = f"{ctx.catalog_name}.{ctx.space}_validation_database.pipeline_validation_report"

            if not spark.catalog._jcatalog.tableExists(validation_table):
                spark.sql(f"""
                     create table {validation_table} using delta as
                     select
                                 batch_id,
                                 pipeline_type,
                                 object_type,
                                 validation_type,
                                 zone,
                                 source_location,
                                 source_database,
                                 source_tablename,
                                 target_database,
                                 target_tablename,
                                 target_column,
                                 source_row_count,
                                 target_row_count,
                                 success_count,
                                 failure_count,
                                 validation_status,
                                 cast('{current_timestamp_val}' as timestamp) as record_created_timestamp,
                                 '{job_log_key}' as record_job_log_key
                     from space_validation_temp_view
                     limit 100
                     """)
            else:
                spark.sql(f"""
                     insert into {validation_table}
                     select
                                 batch_id,
                                 pipeline_type,
                                 object_type,
                                 validation_type,
                                 zone,
                                 source_location,
                                 source_database,
                                 source_tablename,
                                 target_database,
                                 target_tablename,
                                 target_column,
                                 source_row_count,
                                 target_row_count,
                                 success_count,
                                 failure_count,
                                 validation_status,
                                 cast('{current_timestamp_val}' as timestamp) as record_created_timestamp,
                                 '{job_log_key}' as record_job_log_key
                     from space_validation_temp_view
                     limit 100
                                         """)
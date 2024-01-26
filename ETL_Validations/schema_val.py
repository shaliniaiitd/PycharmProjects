import uuid
from datetime import datetime
from typing import Text, List

from pyspark.shell import spark
from pyspark.sql import SparkSession

from we.pipeline.core.util.configuration_util import to_database_name, to_s3_location
from we.pipeline.validation.task.validation_context import ValidationContext


class Validation:
    def validate(self):
        """Validate some test results.
        :return: True if all expectations are met. False if some expectations
        are not met.
        """
        return True

class SchemaValidation(Validation):
    def __init__(self,
                 spark: SparkSession,
                 run_id: Text,
                 use_case_id: Text,
                 validation_context: ValidationContext,
                 s3_folder: Text):
        self.spark = spark
        self.run_id = run_id
        self.use_case_id = use_case_id
        self.validation_context = validation_context
        self.s3_folder = s3_folder

    def validate(self):

        date_time_obj = datetime.utcnow()
        current_timestamp_val = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        job_log_key = str(uuid.uuid4())
        source_schema_view = 'source_schema_temp_view'
        target_schema_view = 'target_schema_temp_view'
        ctx = self.validation_context
        date_time_obj = datetime.utcnow()
        batch_id = self.use_case_id
        success_count = 0
        failure_count = 0
        validation_status = ""


        if (ctx.source_zone is None):
            source_database = None
            target_database = to_database_name(ctx.space, ctx.target_zone, ctx.data_group)

        else:
            source_database = to_database_name(ctx.space, ctx.source_zone, ctx.data_group)
            target_database = to_database_name(ctx.space, ctx.target_zone, ctx.data_group)
            self.s3_folder = None

        # updated s3_location to s3_folder
        if self.s3_folder:
            if ctx.job_type =="onetime":
                df_source_file = spark.read.parquet(self.s3_folder)
                df_source_file.createOrReplaceTempView("temp_view")
                df_source_schema = spark.sql("""desc temp_view""")
                src_cnt = df_source_schema.count()

                df_source_schema.createOrReplaceTempView(source_schema_view)

                df_target_schema = spark.sql(f"""desc {ctx.catalog_name}.{target_database}.{ctx.target_tablename} """)
                df_target_schema.createOrReplaceTempView(target_schema_view)
                tgt_cnt=df_target_schema.count()
            else:
                df_source_file = spark.read.schema("schema_path").parquet(self.s3_folder)
                df_source_file.createOrReplaceTempView("temp_view")
                df_source_schema = spark.sql("""desc temp_view""")
                src_cnt = df_source_schema.count()

                df_source_schema.createOrReplaceTempView(source_schema_view)

                df_target_schema = spark.sql(f"""desc {ctx.catalog_name}.{target_database}.{ctx.target_tablename} """)
                df_target_schema.createOrReplaceTempView(target_schema_view)
                tgt_cnt = df_target_schema.count()

        else:
            df_source_schema = spark.sql(f""" desc {ctx.catalog_name}.{source_database}.{ctx.source_tablename} """)
            src_cnt = df_source_schema.count()
            df_source_schema.createOrReplaceTempView(source_schema_view)

            df_target_schema = spark.sql(f"""desc {ctx.catalog_name}.{target_database}.{ctx.target_tablename}""")
            df_target_schema.createOrReplaceTempView(target_schema_view)
            tgt_cnt = df_target_schema.count()

        default_excluded_columns = [
            '_rescued_data', 'record_created_filename', 'record_created_timestamp',
            'record_job_log_key', 'history_flag', 'longitude', 'latitude', '# Partitioning', 'Not partitioned','src_address_hash','src_address_id_int', 'src_inf_address_id','src_address_id']

        exclude_columns = default_excluded_columns  # + ctx.Exclude_list_col
        column_names_string = ",".join([f" '{x}' " for x in exclude_columns])

        df_schema_validate = spark.sql(f"""
                        select match_flag,
                        count(*) column_count
                        from
                        (
                          select coalesce(source.col_name, target.col_name) as col_name,
                          source.data_type as source_data_type,
                          target.data_type as target_data_type,
                          case when nvl(source.data_type,'') = nvl(target.data_type,'') then
                            'Matched'
                          else
                            'Not Matched'
                          end as match_flag
                          from
                          (
                            select
                            col_name,
                            data_type
                            from source_schema_temp_view
                            where col_name not in 
                              ({column_names_string})
                          ) source
                          full outer join
                          (
                          select
                            col_name,
                            data_type
                            from target_schema_temp_view
                             where col_name not in
                            (
                            {column_names_string}
                            )
                          ) target
                          on source.col_name = target.col_name
                        )
                        group by 1
                        order by 1
                    """)
        match = 'Matched'
        not_match = 'Not Matched'
        Result = df_schema_validate.collect()
        if len(Result) == 1 and Result[0][0] == match:
            failure_count = 0
            success_count = Result[0][1]
            validation_status = "Success"
        elif len(Result) == 1 and Result[0][0] == not_match:
            failure_count = Result[0][1]
            success_count = 0
            validation_status = "Failed"
        elif len(Result) == 2 and Result[0][0] == match:
            success_count = Result[0][1]
            failure_count = Result[1][1]
            validation_status = "Failed"
        elif len(Result) == 2 and Result[1][0] == match:
            success_count = Result[1][1]
            failure_count = Result[0][1]
            validation_status = "Failed"

        db_name = f"{ctx.catalog_name}.{ctx.space}_validation_database"
        spark.sql(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        validation_table = f"{ctx.catalog_name}.{ctx.space}_validation_database.pipeline_validation_report"
        row_schema_view = 'row_schema_check_temp_view'
        df_schema_validate.createOrReplaceTempView(row_schema_view)
        df = spark.sql(f"""   select
                                '{batch_id}' as batch_id,
                                '{ctx.pipeline}' as pipeline_type,
                                '{ctx.object_type}' as object_type,
                                'Schema_validation' as validation_type,
                                 '{ctx.zone}' as zone,
                                 '{self.s3_folder}' as source_location ,
                                 '{source_database}' as source_database,
                                 '{ctx.source_tablename}' as source_tablename,
                                 '{target_database}' as target_database,
                                 '{ctx.target_tablename}' as target_tablename,
                                 'NA' as target_column,                   
                                  '{src_cnt}' as source_row_count,
                                  '{tgt_cnt}' as target_row_count,
                                  '{success_count}' as success_count,
                                  '{failure_count}' as failure_count,
                                  '{validation_status}' as validation_status,
                                  cast('{current_timestamp_val}' as timestamp) as record_created_timestamp,
                                  '{job_log_key}' as record_job_log_key
                                   """)
        df.createOrReplaceTempView("Report_to_table")

        if not spark.catalog._jcatalog.tableExists(validation_table):
            spark.sql(f"""  create table {validation_table} using delta as
                            select * from Report_to_table           
                      """)
        else:
            spark.sql(f""" insert into {validation_table}
                            select * from Report_to_table
                        """)

        # True if all matched
        return (0 < df_schema_validate.count() and
                0 == df_schema_validate.filter("match_flag <> 'Matched'").count())


import uuid
from datetime import datetime
from typing import Text, List

from pyspark.shell import spark
from pyspark.sql import SparkSession

from we.pipeline.core.util.configuration_util import to_database_name, to_s3_location
from we.pipeline.validation.task.validation_context import ValidationContext

class DuplicateValidation:

    def __init__(self,
                 spark: SparkSession,
                 catalog: Text,
                 source_folder: Text,
                 source_database: Text,
                 source_table: Text,
                 target_database: Text,
                 target_table: Text,
                 key_column: List[str],
                 object_type: Text,
                 source_zone: Text,
                 target_zone: Text,
                 pipeline: Text,
                 source_target_list_duplicate_val: List[tuple[str, str, str, str, str, str, str, str, str, str, str]],
                 run_id: str,
                 use_case_id: str):

        self.spark = spark
        self.catalog = catalog
        self.source_folder = source_folder
        self.source_database = source_database
        self.source_table = source_table
        self.target_database = target_database
        self.target_table = target_table
        self.key_column = key_column
        self.object_type = object_type
        self.source_zone = source_zone
        self.target_zone = target_zone
        self.pipeline = pipeline
        self.source_target_list_duplicate_val = source_target_list_duplicate_val
        self.run_id = run_id
        self.use_case_id = use_case_id


class DuplicateValidation:

    def __init__(self,
                 spark: SparkSession,
                 run_id: Text,
                 use_case_id: Text,
                 validation_context: ValidationContext):
        self.spark = spark
        self.run_id = run_id
        self.use_case_id = use_case_id
        self.validation_context = validation_context

    def duplicate_validation(self):
        date_time_obj = datetime.now()
        batch_id = self.use_case_id
        current_timestamp_val = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        job_log_key = str(uuid.uuid4())
        ctx = self.validation_context
        run_id = self.run_id
        pipeline = ctx.pipeline
        object_type = ctx.object_type
        catalog_name = ctx.catalog_name
        target_tablename = ctx.target_tablename
        zone = ctx.zone
        validation_type = "duplicate_check"
        key_columns = ctx.key_column.split(',')
        key_columns_select_parts = [f'{k}' for k in key_columns]
        key_columns_expr = ', '.join(key_columns_select_parts)
        duplicate_check_view = "duplicate_check_temp_view"
        target_database = to_database_name(ctx.space, ctx.target_zone, ctx.data_group)
        df_duplicate_check = spark.sql(f"""
                    select
                    '{batch_id}' as batch_id,
                    '{pipeline}' as pipeline_type,
                    '{object_type}' as object_type,
                    '{validation_type}' as validation_type,
                    '{zone}' as zone,
                    cast('NA' as string) as source_location,
                    cast('NA' as string) as source_database,
                    cast('NA' as string) as source_tablename,
                    a.target_database,
                    a.target_tablename,
                    '{key_columns_expr}' as target_column,
                    null as source_row_count,
                    table_count as target_row_count,
                    (table_count - duplicate_count) as success_count,
                    duplicate_count as failure_count,
                    case 
                        when duplicate_count = 0 then 'Success: No Duplicate Found'
                        else 'Failure: Duplicates Found'
                    end as validation_status,
                    '{current_timestamp_val}' as record_created_timestamp,
                    '{job_log_key}' as job_log_key
                    from
                    (
                        select
                        '{target_database}' as target_database,
                        '{target_tablename}' as target_tablename,
                        '{key_columns_expr}' as key_column,
                        (count(*)) as duplicate_count
                        from
                        (
                            select
                            {key_columns_expr},
                            count(*) as cnt
                            from
                            {catalog_name}.{target_database}.{target_tablename}
                            group by
                            {key_columns_expr}
                            having
                            count(*) > 1
                        )
                    ) a
                    inner join (
                        select
                        '{target_database}' as target_database,
                        '{target_tablename}' as target_tablename,
                        count(*) as table_count
                        from
                        {catalog_name}.{target_database}.{target_tablename}
                    ) b on a.target_database = b.target_database
                    and a.target_tablename = b.target_tablename
          """)

        df_duplicate_check.createOrReplaceTempView(duplicate_check_view)

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
                                from {duplicate_check_view}
                          """)
        else:
            spark.sql(f"""insert into {validation_table}
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
                                from {duplicate_check_view}
                          """)

        return df_duplicate_check

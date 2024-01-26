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


class CountValidation(Validation):
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
        batch_id = self.use_case_id
        current_timestamp_val = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        job_log_key = str(uuid.uuid4())

        source_count_view = 'source_count_temp_view'
        target_count_view = 'target_count_temp_view'
        validation_type = "row_count_check"

        ctx = self.validation_context
        pipeline = ctx.pipeline
        object_type = ctx.object_type
        catalog_name = ctx.catalog_name
        source_tablename = ctx.source_tablename
        target_tablename = ctx.target_tablename
        zone = ctx.zone
        key_column = ctx.key_column

        if (ctx.source_zone is None):
            source_database = None
            target_database = to_database_name(ctx.space, ctx.target_zone, ctx.data_group)

        else:
            source_database = to_database_name(ctx.space, ctx.source_zone, ctx.data_group)
            target_database = to_database_name(ctx.space, ctx.target_zone, ctx.data_group)
            self.s3_folder = None

        # updated s3_location to s3_folder
        if self.s3_folder:
            df_source_file = spark.read.parquet(self.s3_folder)
            df_source_file.createOrReplaceTempView(source_count_view)

            df_target_count = spark.sql(
                f"select * from {ctx.catalog_name}.{target_database}.{ctx.target_tablename}"
            )
            df_target_count.createOrReplaceTempView(target_count_view)
        else:
            if ctx.source_zone == "raw":
                df_source_count = spark.sql(
                    f"select distinct {key_column} from {ctx.catalog_name}.{source_database}.{ctx.source_tablename}"
                )
                df_source_count.createOrReplaceTempView(source_count_view)

                df_target_count = spark.sql(
                    f"select * from {ctx.catalog_name}.{target_database}.{ctx.target_tablename}"
                )
                df_target_count.createOrReplaceTempView(target_count_view)
            else:
                df_source_count = spark.sql(
                    f"select * from {ctx.catalog_name}.{source_database}.{ctx.source_tablename}"
                )
                df_source_count.createOrReplaceTempView(source_count_view)

                df_target_count = spark.sql(
                    f"select * from {ctx.catalog_name}.{target_database}.{ctx.target_tablename}"
                )
                df_target_count.createOrReplaceTempView(target_count_view)

        df_row_count_check = spark.sql(f"""
                    select
                    '{batch_id}' as batch_id,
                    '{pipeline}' as pipeline_type,
                    '{object_type}' as object_type,
                    '{validation_type}' as validation_type,
                    '{zone}' as zone,
                    max(source_location) as source_location,
                    max(source_database) as source_database,
                    max(source_tablename) as source_tablename,
                    max(target_database) as target_database,
                    max(target_tablename) as target_tablename,
                    cast('NA' as string) as target_column,
                    max(source_row_count) as source_row_count,
                    max(target_row_count) as target_row_count,
                    (
                        case
                        when max(source_row_count) >= max(target_row_count) then max(target_row_count)
                        else max(source_row_count)
                        end
                    ) as success_count,
                    (
                        case
                        when max(source_row_count) >= max(target_row_count) then max(source_row_count) - max(target_row_count)
                        else max(target_row_count) - max(source_row_count)
                        end
                    ) as failure_count,
                    (
                        case
                        when nvl(max(source_row_count), 0) = nvl(max(target_row_count), 0) then 'Record count matching between Source and Target'
                        when nvl(max(source_row_count), 0) > nvl(max(target_row_count), 0) then 'Source is having more records compared to Target'
                        else 'Target is having more records compared to Source'
                        end
                    ) as validation_status,
                    '{current_timestamp_val}' as record_created_timestamp,
                    '{job_log_key}' as job_log_key
                    from
                    (
                        select
                        '{self.s3_folder}' as source_location,
                        '{source_database}' as source_database,
                        '{source_tablename}' as source_tablename,
                        count(*) as source_row_count,
                        cast(null as string) as target_database,
                        cast(null as string) as target_tablename,
                        cast(null as integer) as target_row_count
                        from
                        {source_count_view}
                        union all
                        select
                        null as source_location,
                        cast(null as string) as source_database,
                        cast(null as string) as source_tablename,
                        cast(null as integer) as source_row_count,
                        '{target_database}' as target_database,
                        '{target_tablename}' as target_tablename,
                        count(*) as target_row_count
                        from
                        {target_count_view}
                    )
                """)

        row_count_view = 'row_count_check_temp_view'
        df_row_count_check.createOrReplaceTempView(row_count_view)
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
                from {row_count_view}
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
                from {row_count_view}
            """)

        # True if all matched
        return (0 < df_row_count_check.count() and
                0 == df_row_count_check.filter(
                    "validation_status <> 'Record count matching between Source and Target'").count())


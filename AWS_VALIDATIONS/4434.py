import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Glue job parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job.init(args['JOB_NAME'])

# Initialize logger
# logger = glueContext.get_logger()
# logger.info(f"jobname = {args['JOB_NAME']}")

conn_s3_path = 's3://alt-we-tgt-dev-v1/we/dev/feature/conn/conn_mapping_out/delta/00000000'
all_social_s3_path = 's3://alt-we-tgt-dev-v1/we/dev/feature/conn/all_social/delta/00000000'


def not_match_conn_all_social(conn_s3_path, all_social_s3_path, source, type):
    # global logger
    logger = glueContext.get_logger()
    # logger.info("THis is a log entry")

    # Read from Conn Mapping Output
    conn_map_dyf = glueContext.create_dynamic_frame.from_options(
        's3',
        connection_options={"paths": [conn_s3_path]},
        format='parquet',
        format_options={"compression": 'snappy'},
        transformation_ctx="from_s3"
    )

    # # convert dynamic frame to a spark frame
    conn_map_df = conn_map_dyf.toDF()
    df1 = conn_map_df.filter(conn_map_df['type'] == type)

    # conn_map_df.printSchema()

    all_social_dyf = glueContext.create_dynamic_frame.from_options(
        's3',
        connection_options={"paths": [all_social_s3_path]},
        format='parquet',
        format_options={"compression": 'snappy'},
        transformation_ctx="from_all_social"
    )

    # # convert dynamic frame to a spark frame
    all_social_s3_df = all_social_dyf.toDF()

    # logger.info("TOTAL NUMBER OF RECORDS AT all_social = ", all_social_s3_df.count())

    # Filter by source and type
    df2 = all_social_s3_df.filter((all_social_s3_df['source'] != source) & (all_social_s3_df['type'] == type))

    # logger.info(f"All social count for source = {source} and type = {type} = {df2.count()}" )

    df2_rows_not_in_df1 = df2.join(df1, 'we_pid', 'left_anti')

    # Perform the inner join operation to check if all data matches
    joined_df = df2.join(df1, (df1['type'] == df2['type']) &
                         (df2['type'] == type) &
                         (df1['we_pid'] == df2['we_pid']) &
                         (df1['link_pid'] == df2['cof_we_pid']), 'inner')

    # logger.info(f"joined count for source {source} and type {type} = {joined_df.count()} and df2.count() = {df2.count()}")

    # Assert that all rows in all_social match with conn_mapping data
    assert joined_df.count() == 0 and df2_rows_not_in_df1.count() == df2.count(), f"FAILURE: {df1.count()} all_social records found in CONN_MAPPING_OUT for type {type} and source !={source}"

    print(f"SUCCESS:NO SOCIAL RECORDS FOUND IN CONN_MAPPING_OUT for type = {type}")


not_match_conn_all_social(conn_s3_path, all_social_s3_path, 10, 2)
not_match_conn_all_social(conn_s3_path, all_social_s3_path, 10, 3)

job.commit()
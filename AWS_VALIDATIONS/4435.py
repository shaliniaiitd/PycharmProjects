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
logger = glueContext.get_logger()
logger.info(f"jobname = {args['JOB_NAME']}")

conn_s3_path = 's3://alt-we-tgt-dev-v1/we/dev/feature/conn/conn_mapping_out/delta/00000000'
all_social_s3_path = 's3://alt-we-tgt-dev-v1/we/dev/feature/conn/all_social/delta/00000000'
ppm_s3_path = 's3://alt-we-tgt-dev-v1/we/dev/feature/master/org_ppl/delta/00000000'


def read_from_s3(s3_path, view_name):
    # Read from Conn Mapping Output
    dyf = glueContext.create_dynamic_frame.from_options(
        's3',
        connection_options={"paths": [s3_path]},
        format='parquet',
        format_options={"compression": 'snappy'},
        transformation_ctx="from_s3"
    )

    # convert dynamic frame to a spark frame
    df = dyf.toDF()

    view = df.createOrReplaceTempView(view_name)

    return view


conn_map_view = read_from_s3(conn_s3_path, 'conn_map_view')
all_social_view = read_from_s3(all_social_s3_path, 'all_social_view')
ppm_view = read_from_s3(ppm_s3_path, 'ppm_view')

filtered_df = spark.sql(f"SELECT c.we_pid,c.link_pid FROM conn_map_view c,\
            all_social_view s \
            WHERE s.we_pid = c.we_pid \
            and s.cof_we_pid = c.link_pid \
            and s.source != 10 \
            and s.type = c.type \
            and c.type = 4")

filtered_view = filtered_df.createOrReplaceTempView('filtered_view')

##################
# VALIDATIONS
##################

# Validate address match

val_addr = spark.sql(f"select count(*) from filtered_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and ppm1.we_addr_id != ppm2.we_addr_id")

if val_addr.collect()[0][0] != 0:
    print(f"FAILURE: {val_addr.collect()[0][0]} records of type 4 have different addreses")
else:
    print("SUCCESS: address matches for all records of type 4")

# Validate last name match

val_ln = spark.sql(f"select count(*) from filtered_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and ppm1.last_name != ppm2.last_name")

if val_ln.collect()[0][0] != 0:
    print(f"FAILURE: {val_ln.collect()[0][0]} records of type 4 have different last names")
else:
    print("SUCCESS: last names for all records of type 4 match")

pd_s3_path = 's3://alt-we-tgt-dev-v1/we/dev/feature/summary/person_details/delta/00000000/'
pd_view = read_from_s3(pd_s3_path, 'pd_view')

val_age = spark.sql(f"select count(*) from filtered_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and ((ppm1.birth_year IS NOT NULL) and (ppm2.birth_year IS NOT NULL))")

if val_age.collect()[0][0] != 0:
    print(f"FAILURE: {val_age.collect()[0][0]} records of type 4 have known age gap")
else:
    print("SUCCESS: age gap for all records of type 4 are UNKNOWN")

job.commit()
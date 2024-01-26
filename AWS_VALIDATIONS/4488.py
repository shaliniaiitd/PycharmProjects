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

# 1: type 5 non-matching org_id

filtered_df = spark.sql(f"SELECT count(*) FROM conn_map_view c,\
            ppm_view p1, ppm_view p2 \
            WHERE c.we_pid = p1.we_pid \
            and  c.link_pid = p2.we_pid\
            and c.type = 5 \
            and p1.we_org_id != p2.we_org_id")

fail_count = filtered_df.collect()[0][0]

if fail_count == 0:
    print(f"SUCCESS: All connection type 5 have matching org_id")

else:
    print(f"FAILURE: {fail_count} connections of type 5 not found to have matching org_id")

# 2: type 6 non-matching org_id
filtered_df = spark.sql(f"SELECT count(*) FROM conn_map_view c,\
            ppm_view p1, ppm_view p2 \
            WHERE c.we_pid = p1.we_pid \
            and  c.link_pid = p2.we_pid\
            and c.type = 6 \
            and p1.we_org_id != p2.we_org_id")

fail_count = filtered_df.collect()[0][0]

if fail_count == 0:
    print(f"SUCCESS: All connection type 6 have matching org_id")

else:
    print(f"FAILURE: {fail_count} connections of type  6 not found to have matching org_id")

# 3 Validate org_id count

df = spark.sql(f"SELECT p1.we_org_id,count(p1.we_org_id) as org_id_count,c.type FROM conn_map_view c,\
            ppm_view p1, ppm_view p2 \
            WHERE c.we_pid = p1.we_pid \
            and  c.link_pid = p2.we_pid\
            and c.type in (5,6) \
            and p1.we_org_id = p2.we_org_id \
            group by p1.we_org_id, c.type")

filtered_df = df.filter((df["org_id_count"] < 2) | (df["org_id_count"] > 100))

fail_count = filtered_df.count()

if fail_count == 0:
    print(f"SUCCESS: All type 5/6 records have org_id count <100 and > 2")

else:
    print(f"FAILURE: {fail_count} type 5/6 records have org_id count >100 or < 2")

# 4 Validate correct allocation of type 5

val_type5_null = spark.sql(f"select count(*) from conn_map_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and (ppm1.exec_flag IS NULL and ppm1.owner_flag IS NULL and ppm2.exec_flag IS NULL and ppm2.owner_flag IS NULL) \
and c.type = 5"
                           )

fail_count = val_type5_null.collect()[0][0]
if fail_count == 0:
    print(f"SUCCESS: None of the records of type 5 have null exec and owner flags.")

else:
    print(f"FAILURE: {fail_count} records have null exec and owner flags but assigned type 5")

# 5
val_type5_false = spark.sql(f"select count(*) from conn_map_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and (ppm1.exec_flag== 'False' and ppm1.owner_flag== 'False' and  ppm2.exec_flag == 'False' and ppm2.owner_flag == 'False') \
and c.type = 5"
                            )

fail_count = val_type5_false.collect()[0][0]
if fail_count == 0:
    print(f"SUCCESS: None of the records of type 5 have exec and owner flags as false.")

else:
    print(f"FAILURE: {fail_count} records have both exec and owner flags as false but assigned type 5")

# 6
val_type5_swap = spark.sql(f"select count(*) from conn_map_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and (ppm1.exec_flag== 'True' or ppm1.owner_flag== 'True' or  ppm2.exec_flag == 'True' or ppm2.owner_flag == 'True') \
and c.type = 6"
                           )

fail_count = val_type5_swap.collect()[0][0]
if {fail_count} == 0:
    print(f"SUCCESS: None of the records of type 5 is swaped as type6.")

else:
    print(f"FAILURE: {fail_count} records qualify for type 5 but assigned type6.")

########################################
# Validate correct allocation of type 6
########################################

# 7
val_type6_null = spark.sql(f"select count(*) from conn_map_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and (ppm1.bod_flag IS NULL and ppm1.trustee_flag IS NULL and ppm2.bod_flag IS NULL and ppm2.trustee_flag IS NULL) \
and c.type = 6"
                           )

fail_count = val_type6_null.collect()[0][0]
print(fail_count)
if {fail_count} == 0:
    print(f"SUCCESS: None of the records of type 6 have null bod and trustee flags.")
else:
    print(f"FAILURE: {fail_count} records have null bod and trustee flags but assigned type 6")

# 8
val_type6_false = spark.sql(f"select count(*) from conn_map_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and (ppm1.bod_flag== 'False' and ppm1.trustee_flag== 'False' and  ppm2.bod_flag == 'False' and ppm2.trustee_flag == 'False') \
and c.type = 6"
                            )

fail_count = val_type6_false.collect()[0][0]
print(fail_count)
if {fail_count} == 0:
    print(f"SUCCESS: None of the records of type 6 have bod and trustee flags as false.")

else:
    print(f"FAILURE: {fail_count} records have both bod and trustee flags as false but assigned type 6")

# 9
val_type6_swap = spark.sql(f"select count(*) from conn_map_view c, ppm_view ppm1, ppm_view ppm2 \
where c.we_pid =ppm1.we_pid \
and c.link_pid = ppm2.we_pid \
and (ppm1.bod_flag== 'True' or ppm1.trustee_flag== 'True' or  ppm2.bod_flag == 'True' or ppm2.trustee_flag == 'True') \
and c.type = 5"
                           )

fail_count = int(val_type6_swap.collect()[0][0])
print(fail_count)
if {fail_count} == 0:
    print(f"SUCCESS: None of the records of type 6 is swapped as type5.")
else:
    print(f"FAILURE: {fail_count} records qualify for type 6 but assigned type5.")

job.commit()


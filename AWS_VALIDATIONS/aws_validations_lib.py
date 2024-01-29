import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import current_timestamp
from awsglue.dynamicframe import DynamicFrame

import psycopg2
import boto3

table = 'employee'
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'])

## @params: [JOB_NAME]
## @params: [S3_PATH] - Path cotaining s3 bucket, s3 folder and the file name(to be counted).
## @params: [CONNECTION_NAME] - JDBC connection to Postgresql
## @params: [TABLE_NAME] - Postgresql table whose records need to be counted.
##

# Glue job parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_PATH', 'CONNECTION_NAME'])
# ,'TABLE_NAME'])

job.init(args['JOB_NAME'], args)

####################################
# Read/Derive Inputs from arguments
####################################
print(f"jobname = {args['JOB_NAME']}")
# get Direct inputs
s3_path = args['S3_PATH']
# table = args['TABLE_NAME']
connection_name = args['CONNECTION_NAME']

# #s3_path = 's3://alt-we-tgt-dev-v1/misc/test/data/pos/20230701/data.csv'
# #s3_path = 's3://alt-we-tgt-dev-v1/misc/test/qa_poc/20220217_143158_00011_dnh83_1853680f-400b-4d90-8f1c-e4af859683c8.parquet'
# #s3_path = 's3://alt-we-tgt-dev-v1/misc/test/qa_poc/part-00000-19a33966-8750-4518-9cee-2f4a1d3c1483-c000.snappy.parquet'

# print(f"s3_path={s3_path},table= {table},connection_name={connection_name}")
def extract_s3_params(s3_path):
    # Extract s3 related parameters
    s3_path_parts = s3_path.split('/')
    del s3_path_parts[0]
    del s3_path_parts[0]

    # file_name = s3_path_parts.pop()
    s3_bucket = s3_path_parts.pop(0)
    s3_key = ('/').join(s3_path_parts)

    print(f"s3_bucket = {s3_bucket}, s3_key = {s3_key}")

def get_s3_file_list(s3_bucket,s3_key):
    # Get filenames under s3 folder

    # # Initialize the S3 client
    client = boto3.client('s3')

    # # List objects in the specified folder
    response = client.list_objects_v2(Bucket=s3_bucket, Prefix=s3_key)

    # # Extract the filenames from the response
    filenames = [obj['Key'] for obj in response.get('Contents', [])]

    del filenames[0]  # getting rid of the folder name

    print("All filenames", filenames)

def get_options(file_name):
    format = file_name.split('.')[-1]
    compression = file_name.split('.')[-2]

    format_options = {}
    if format == 'csv':
        format_options = {"separator": ',', "withHeader": True, }
    elif format == 'parquet':
        format_options = {"compression": compression, }
    print(f"filename = {file_name}, format = {format}, compression= {compression}")

    options = {'s3_filename':file_name, 'format':format,'format_options': format_options }

    return options

def get_s3_count(s3_path,options):

    # #########################################
    # # Read Input data count from S3 file
    # #########################################

    # Read the Input file data into a DynamicFrame
    src_dyf = glueContext.create_dynamic_frame.from_options(
        's3',
        connection_options={"paths": [s3_path]},
        format=options['format'],
        format_options=options['format_options'],
        transformation_ctx="from_s3"
    )

    # convert dynamic frame to a spark frame
    s3_df = src_dyf.toDF()

    s3_df.printSchema()
    s3_df.show()

    # Get count of the Frame
    s3_count = s3_df.count()
    print(f"Total records at s3, in {format} format are {s3_count}")

    ########################################
    # Load s3 test data into Postgres table
    #######################################

    # # # Extract Postgresql parameters

    jdbc_conf = glueContext.extract_jdbc_conf(connection_name=connection_name)
    print(jdbc_conf)
    jdbc_url = jdbc_conf['fullUrl']
    username = jdbc_conf['user']
    password = jdbc_conf['password']
    dbname = jdbc_url.split('/')[-1]
    port = jdbc_url.split(':')[-1].split('/')[0]
    host = jdbc_url.split(':')[2][2::]
    print(f"jdbc_url = {jdbc_url}, username = {username}, password = {password}, dbname = {dbname}, port = {port}, host = {host}")
    print(f"LOADING {src_dyf.toDF().count()} rows from src_dyf in PG table")

    glueContext.write_dynamic_frame.from_jdbc_conf(frame=src_dyf,
                                                   catalog_connection=connection_name,
                                                   connection_options={"dbtable": "employee", "database": dbname},
                                                   transformation_ctx="test_data_uploaded")
    print("TEST DATA LOADED IN PG TABLE")

    # #################################
    # # Get count from Postgres table
    # #################################
    # print("TABLE_NAME:" ,table)

    # ###############
    # # Approach-1
    # ##############

    # # SQL query to count rows in the table
    # # query = f"SELECT COUNT(*) FROM {table};"

    # # print(query)

    # # conn = psycopg2.connect(
    # #     database=dbname,
    # #     user=username,
    # #     password=password,
    # #     host= host,
    # #     port=port
    # # )

    # # conn.autocommit = True
    # # cursor = conn.cursor()

    # # cursor.execute(query)
    # # pg_count = cursor.fetchall()[0][0]

    # # # Print the result
    # # print(pg_count)

    # # conn.commit()
    # # conn.close()

def get_postgres_df(jdbc_url,table,username,password):
    # ################################
    # # Get dataframe from postgresql
    # ################################

    connection_options = {
        "url": jdbc_url,
        "dbtable": "employee",
        "user": username,
        "password": password,
    }

    pg_dyf = glueContext.create_dynamic_frame.from_options(
        connection_type='postgresql',
        connection_options=connection_options
    )

    # # Convert DynamicFrame to DataFrame
    pg_df = pg_dyf.toDF()

    # # Count the number of records in the DataFrame
    pg_count = pg_df.count()

    # Print the record count
    print(f"Number of records in '{table}': {pg_count}")

    # ##################
    # # validate schema
    # ##################
    compare_schemas(s3_df, pg_df)

# # ################################
#     # # Perform data integrity check
#     # ################################
#
#     result_df = s3_df.exceptAll(pg_df)  # preserve duplicates
#     diff = result_df.count()
#
#     print(f"Following {diff} rows are in s3_df but not in pg_df: {result_df.show()}")
#
#     result2_df = pg_df.exceptAll(s3_df)
#     print(f"Following {result2_df.count()} rows are in pg_df but not in s3_df: {result2_df.show()}")


def compare_schemas(df1: DataFrame, df2: DataFrame):
    schema1 = df1.schema
    schema2 = df2.schema

    if schema1 == schema2:
        print("The schemas of the two DataFrames are identical.")
    else:
        print("The schemas of the two DataFrames are different.")

        # Find the differences in fields
        fields1 = set(field.name for field in schema1.fields)
        fields2 = set(field.name for field in schema2.fields)

        fields_only_in_1 = fields1 - fields2
        fields_only_in_2 = fields2 - fields1

        if fields_only_in_1:
            print("Fields only in DataFrame 1:")
            for field in fields_only_in_1:
                print(field)

        if fields_only_in_2:
            print("Fields only in DataFrame 2:")
            for field in fields_only_in_2:
                print(field)


from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
import hashlib

# Initialize contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Create DataFrames
df1 = spark.read.format("csv").option("header", "true").load("s3://your-bucket/path/to/df1.csv")
df2 = spark.read.format("csv").option("header", "true").load("s3://your-bucket/path/to/df2.csv")


def calculate_checksum(row):
    # Calculate MD5 checksum for each row in a DataFrame
    checksum = hashlib.md5()
    for value in row:
        checksum.update(str(value).encode('utf-8'))
    return checksum.hexdigest()

# Add a checksum column to DataFrames
s3_df_with_checksum = s3_df.withColumn("checksum", calculate_checksum(df1.columns))
pg_df_with_checksum = pg_df.withColumn("checksum", calculate_checksum(df2.columns))

# Compare DataFrames using checksums
diff_df = df1_with_checksum.join(df2_with_checksum, on=["checksum"], how="outer").filter("df1.checksum IS NULL OR df2.checksum IS NULL")

print(f"Following {diff_df.count()} rows do not have same column values across s3 and postgrsql: ")

# Show differing rows
diff_df.show()

# Stop Spark context
sc.stop()



# Call the function to compare schemas
compare_schemas(s3_df, pg_df)

# # #get the schemas
# print('COMPARING SCHEMA')
# s3_schema = s3_df.schema()
# pg_schema = pg_df.schema()
#
# # Compare the schemas
# if s3_schema == pg_schema:
#     print("The source and target schemas are identical.")
# else:
#     print("The source and target schemas are different.")
#
#     # Print the differences between the schemas
#     diff_fields = set(s3_schema.fields) ^ set(pg_schema.fields)
#
#     print("Fields present in s3_schema but not in pg_schema:",
#           [field.name for field in diff_fields if field in s3_schema.fields])
#
#     print("Fields present in pg_schema but not in s3_schema:",
#           [field.name for field in diff_fields if field in pg_schema.fields])
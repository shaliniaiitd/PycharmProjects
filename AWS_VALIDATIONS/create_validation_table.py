import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

# Initialize Glue context and Spark context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

dbname = "wedatahub"
user = "wedatahub"
password = "chBVGNyC6VefLJHDLPvkgnHu"
host = "we-data-hub-dev-cluster.cluster-c5bal8i1ijfc.us-east-1.rds.amazonaws.com"
port = "5432"
table_name = "employee"
# Database connection parameters
db_params = {
    "url": f"jdbc:postgresql://{host}:{port}/{dbname}",
    "user": user,
    "password": password,
k    "dbtable": table_name
}

# Table creation SQL
create_table_sql = """
    CREATE TABLE IF NOT EXISTS table_name (
        id serial PRIMARY KEY,
        name varchar(255),
        age integer
    )
"""

# Sample data to insert
sample_data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 28)
]

def main():
    # Create the table if it doesn't exist
    spark.read \
        .format("jdbc") \
        .option("url", db_params["url"]) \
        .option("user", db_params["user"]) \
        .option("password", db_params["password"]) \
        .option("dbtable", db_params["dbtable"]) \
        .option("driver", "org.postgresql.Driver") \
        .option("query", create_table_sql) \
        .load()

    # Insert sample data
    df = spark.createDataFrame(sample_data, ["name", "age"])
    df.write \
        .format("jdbc") \
        .option("url", db_params["url"]) \
        .option("user", db_params["user"]) \
        .option("password", db_params["password"]) \
        .option("dbtable", db_params["dbtable"]) \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

if __name__ == "__main__":
    main()

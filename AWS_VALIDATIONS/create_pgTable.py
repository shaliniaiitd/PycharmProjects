from sqlalchemy import create_engine, MetaData, Table, Column, String

# PostgreSQL database connection details
database = "wedatahub"
user = "wedatahub"
password = "chBVGNyC6VefLJHDLPvkgnHu"
host = "we-data-hub-dev-cluster.cluster-c5bal8i1ijfc.us-east-1.rds.amazonaws.com"
port = "5432"

# Name of the new table
table_name = "employee_csv"
# Create a PostgreSQL engine
db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(db_url)

# Create a metadata object
metadata = MetaData()

# Define the table structure
employee_table = Table(
    table_name,
    metadata,
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    create='True'
)

# Create the table in the database
metadata.create_all(engine)

print(f"Table '{table_name}' created successfully.")

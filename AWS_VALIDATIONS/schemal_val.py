import pandas as pd

# Load the Excel sheet into a DataFrame
excel_file = 'mapping.xlsx'
sheet_name = 'property'
excel_df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Define a sample database table schema (you should retrieve this from your database)
# In this example, I'm creating a DataFrame with column names and data types
db_schema = pd.DataFrame({
    'column_name': ['column1', 'column2', 'column3'],
    'data_type': ['int', 'varchar(255)', 'date']
})

# Extract column names and data types from the Excel DataFrame
excel_column_names = excel_df['AB'].tolist()
excel_data_types = excel_df['AC'].tolist()

# Compare Column Names and Data Types
columns_match = excel_column_names == db_schema['column_name'].tolist()
data_types_match = excel_data_types == db_schema['data_type'].tolist()

# Check for Missing Columns
missing_columns_in_excel = set(db_schema['column_name']) - set(excel_column_names)
missing_columns_in_db = set(excel_column_names) - set(db_schema['column_name'])

# Validate Number of Columns
num_columns_match = len(excel_column_names) == len(db_schema)

# Print the results
if columns_match and data_types_match and not missing_columns_in_excel and not missing_columns_in_db and num_columns_match:
    print("Schema validation successful. The schema matches.")
else:
    print("Schema validation failed. Please check the schema definitions.")
    if not columns_match:
        print("Column names do not match.")
    if not data_types_match:
        print("Data types do not match.")
    if missing_columns_in_excel:
        print(f"Missing columns in Excel: {missing_columns_in_excel}")
    if missing_columns_in_db:
        print(f"Missing columns in Database: {missing_columns_in_db}")
    if not num_columns_match:
        print("Number of columns does not match.")

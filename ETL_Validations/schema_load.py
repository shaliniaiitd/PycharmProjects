import json

from importlib import resources as pkg_resources
from pyspark.shell import spark
from pyspark.sql.types import StructType, ArrayType, StringType


def csv_source_file(csv_source_file):
    parameter_delimfile_path = csv_source_file  # Give the location of the csv file
    parameter_delimfile_header = 'false'
    parameter_delimfile_delimiter = '\t'  # choose a delimiter where it is not part of the data
    parameter_delimfile_quote = '"'
    parameter_delimfile_escape = '\"'
    parameter_delimfile_parserLib = 'commons'
    parameter_delimfile_mode = 'PERMISSIVE'
    parameter_delimfile_charset = 'UTF-8'
    parameter_delimfile_inferSchema = 'false'
    parameter_delimfile_comment = ''
    parameter_delimfile_nullValue = ''
    parameter_delimfile_dateFormat = 'yyyy-MM-dd HH:mm:ss'
    parameter_delimfile_multiLine = 'false'

    # Read csv file into dataframe
    df_read_csv_file = spark.read.format('csv').options(header=parameter_delimfile_header,
                                                        delimiter=parameter_delimfile_delimiter,
                                                        quote=parameter_delimfile_quote,
                                                        escape=parameter_delimfile_escape,
                                                        parserLib=parameter_delimfile_parserLib,
                                                        mode=parameter_delimfile_mode,
                                                        charset=parameter_delimfile_charset,
                                                        inferSchema=parameter_delimfile_inferSchema,
                                                        comment=parameter_delimfile_comment,
                                                        nullValue=parameter_delimfile_nullValue,
                                                        dateFormat=parameter_delimfile_dateFormat,
                                                        multiLine=parameter_delimfile_multiLine).load(
        parameter_delimfile_path)

    df_read_csv_file.createOrReplaceTempView("sample_temp_view")
    df_table = add_headers("sample_temp_view")
    return df_table


def add_headers(source_table):
    config = json.loads(pkg_resources.read_text('we.pipeline.core.donation.schema', 'dd_don_schema.json'))
    return config


# def schema_load():
#     """CSV to Parquet.
#
#     To be run at the project root folder.
#     """
#
#     objects = {
#         'aa': 'additional_asset',
#         'ci': 'contact_info',
#         'it': 'investment_transaction',
#         'oa': 'other_attribute',
#         're': 'real_estate',
#         'ri': 'residential_info',
#         'don': 'donation',
#         'pos': 'position'
#     }
#
#     for t, object_name in objects.items():
#         # Load schema
#         with open(f'we/pipeline/{object_name}/schema/dd_{t}_schema.json') as f:
#             schema = StructType.fromJson(json.load(f))
#         # Convert unsupported array type to string
#         for f in schema:
#             if isinstance(f.dataType, ArrayType):
#                 f.dataType = StringType()

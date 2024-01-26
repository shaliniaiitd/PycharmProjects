import re
from datetime import datetime
from typing import Text

from pyspark.shell import spark
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import length, col

from we.pipeline.core.util.configuration_util import to_database_name
from we.pipeline.validation.task.validation_context import ValidationContext

func_config = {
    1: {'error_message': 'FAIL: Found special character. Column is: {column}',
        'func_name': 'name_check_vendor_data_val',
        'temp_view': 'Fail_Result_name_check',
        'temp_viewP': 'Pass_Result_name_check'},
    2: {'error_message': 'FAIL: Found special character. Column is: {column}',
        'func_name': 'address_check_vendor_data_val',
        'temp_view': 'Fail_Result_addr_check',
        'temp_viewP': 'Pass_Result_addr_check'},
    3: {'error_message': 'FAIL: Found Prefix or Suffix. Column is: {column}',
        'func_name': 'suffixPrefix_check_vendor_data_val',
        'temp_view': 'Fail_Result_presuffix_check',
        'temp_viewP': 'Pass_Result_pressufix_check'},
    4: {'error_message': 'FAIL: Found wrong zip or zip4. Column is: {column}',
        'func_name': 'zip_check_vendor_data_val',
        'temp_view': 'Fail_Result_zip_check',
        'temp_viewP': 'Pass_Result_zip_check'},
    5: {'error_message': 'FAIL: Found wrong batchID format. Column is: {column}',
        'func_name': 'batchID_check_vendor_data_val',
        'temp_view': 'Fail_Result_batchID_check',
        'temp_viewP': 'Pass_Result_batchID_check'},
    6: {'error_message': 'FAIL: Found wrong state format. Column is: {column}',
        'func_name': 'state_check_vendor_data_val',
        'temp_view': 'Fail_Result_state_check',
        'temp_viewP': 'Pass_Result_state_check'},
    7: {'error_message': 'FAIL: Found wrong gender format. Column is: {column}',
        'func_name': 'gender_check_vendor_data_val',
        'temp_view': 'Fail_Result_gender_check',
        'temp_viewP': 'Pass_Result_gender_check'},
    8: {'error_message': 'FAIL: Found wrong DOB format. Column is: {column}',
        'func_name': 'DOB_check_vendor_data_val',
        'temp_view': 'Fail_Result_dob_check',
        'temp_viewP': 'Pass_Result_dob_check'},
    9: {'error_message': 'FAIL: Found space. Column is: {column}',
        'func_name': 'space_check_vendor_data_val',
        'temp_view': 'Fail_Result_space_check',
        'temp_viewP': 'Pass_Result_space_check'},
    10: {'error_message': 'FAIL: Cleanup missing. Column is: {column}',
        'func_name': 'cleanup_check_vendor_data_val',
        'temp_view': 'Fail_Result_cleanup_check',
        'temp_viewP': 'Pass_Result_cleanup_check'}
}


class VendorDataValidation:

    def __init__(self,
                 spark: SparkSession,
                 run_id: Text,
                 df: DataFrame,
                 config,
                 config_silver,
                 validation_context: ValidationContext
                 ):

        self.spark = spark
        self.run_id = run_id
        self.df = df
        self.config = config
        self.config_silver = config_silver
        self.validation_context = validation_context

    def validate(self):
        ctx = self.validation_context
        for c in self.df.columns:
            # all = self.config_silver.get(ctx.data_group)
            all = self.config_silver[f'{ctx.data_group}']
            for key, patterns in all.items():
                if key == "__common" or key == ctx.target_tablename:
                    for pat, funcs in patterns.items():
                        if re.match(pat, c):
                            for f in funcs:
                                if f == 'check_batchID':
                                    self.check_batchID(self.df, c, self.run_id, pat)
                                elif f == 'check_func_regex':
                                    self.check_func_regex(self.df, c, self.run_id, pat)
                                elif f == 'check_func_regex_addr':
                                    self.check_func_regex_addr(self.df, c, self.run_id, pat)
                                elif f == 'check_func_regex_presuffix':
                                    self.check_func_regex_presuffix(self.df, c, self.run_id, pat)
                                elif f == 'check_state':
                                    self.check_state(self.df, c, self.run_id, pat)
                                elif f == 'check_func_zip':
                                    self.check_func_zip(self.df, c, self.run_id, pat)
                                elif f == 'check_gender':
                                    self.check_gender(self.df, c, self.run_id, pat)
                                elif f == 'check_dob':
                                    self.check_dob(self.df, c, self.run_id, pat)
                                elif f == 'check_space':
                                    self.check_space(self.df, c, self.run_id, pat)
                                elif f == 'check_cleanup':
                                    self.check_cleanup(self.df, c, self.run_id, pat)

    def check_store_result(self, func_id, check_result, df, col):
        date_time_obj = datetime.utcnow()
        current_timestamp_val = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        ctx = self.validation_context
        target_database = to_database_name(ctx.space, ctx.target_zone, ctx.data_group)
        source_database = to_database_name(ctx.space, ctx.source_zone, ctx.data_group)

        f = func_config[func_id]
        error_message = f['error_message'].format(column=col)
        func_name = f['func_name']
        temp_view = f['temp_view']
        temp_viewP = f['temp_viewP']

        if check_result > 0:
            df.createOrReplaceTempView(temp_view)
            new_df1 = spark.sql(f"""
                       select 
                       max('{func_id}') as func_id,
                       max('{check_result}') as validation_count,
                       max('{col}') as column, 
                       cast('{current_timestamp_val}' as timestamp) as record_created_timestamp,
                       '{error_message}' as status
                       from {temp_view}
                                       """)
        else:
            pass_message = 'Pass'
            df.createOrReplaceTempView(temp_viewP)
            new_df1 = spark.sql(f"""
                       select 
                       max('{func_id}') as func_id,
                       max('{check_result}') as validation_count,
                       max('{col}') as column, 
                       cast('{current_timestamp_val}' as timestamp) as record_created_timestamp,
                       '{pass_message}' as status
                       from {temp_viewP}
                                       """)

        new_df1.createOrReplaceTempView("vendor_data_check_temp_view")
        db_name = f"{ctx.catalog_name}.{ctx.space}_validation_database"
        spark.sql(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        date_time_obj = datetime.now()
        batch_id = date_time_obj.strftime("%Y%m%d%H%M%S")
        validation_table = f"{ctx.catalog_name}.{ctx.space}_validation_database.vendor_validation_report"
        if not spark.catalog._jcatalog.tableExists(validation_table):
            spark.sql(f"""create table {validation_table} using delta as
                              select
                              '{batch_id}'  as batch_id,
                              '{ctx.object_type}' as object_type,
                              '{target_database}' as database, 
                              '{ctx.source_tablename}' as tablename,
                              '{func_name}' as funtion_name,
                              '{col}' as test_case, 
                              func_id, 
                              validation_count, 
                              record_created_timestamp, 
                              status
                              from vendor_data_check_temp_view
                            """)
        else:
            spark.sql(f"""insert into {validation_table}
                            select
                            '{batch_id}'  as batch_id,
                            '{ctx.object_type}' as object_type,
                            '{target_database}' as database,
                            '{ctx.source_tablename}' as tablename,
                            '{func_name}' as funtion_name,
                            '{col}' as test_case, 
                            func_id, 
                            validation_count, 
                            record_created_timestamp, 
                            status
                            from vendor_data_check_temp_view
                            """)
        return new_df1

    # Name Transformation Validation------------------------------------------------------------------------------------
    def check_func_regex(self,
                         df: DataFrame,
                         column: Text,
                         run_id: Text,
                         pat: Text):

        global name_check
        func_id = 1
        m = re.match(pat, column)
        if m:
            name_type = m.group(1)
            if name_type == 'middle':
                name_check = df.where(f"""{column} rlike r"(.*[^a-zA-Z\-\s\',].*|^\w-\w$)" """).count()
                df_name_check = df.where(f"""{column} rlike r"(.*[^a-zA-Z\-\s\',].*|^\w-\w$)" """)
            else:
                name_check = self.df.where(f"""{column} rlike r"(.*[^a-zA-Z\s\',].*)" """).count()
                df_name_check = self.df.where(f"""{column} rlike r"(.*[^a-zA-Z\s\',].*)" """)

        # print('value of check2: ', name_check)
        self.check_store_result(func_id, name_check, df, column)

    # Address Transformation Validation---------------------------------------------------------------------------------
    def check_func_regex_addr(self,
                              source_data: DataFrame,
                              column: Text,
                              run_id: Text,
                              pat: Text):
        func_id = 2

        addr_check = self.df.where(
            column + r" rlike r'(.*[^0-9A-Z@%#,./&_-]\s.*|^\w-\w$|^[^0-9a-zA-Z]+$)'").count()
        df_addr_check = source_data.where(column + " rlike r'(.*[^0-9A-Z@%#,./&_-]\s.*|^\w-\w$|^[^0-9a-zA-Z]+$)'")
        # print('value of check2: ', addr_check)
        self.check_store_result(func_id, addr_check, source_data, column)

    # Pre-Suffix Validation---------------------------------------------------------------------------------------------
    def check_func_regex_presuffix(self,
                                   source_data: DataFrame,
                                   column: Text,
                                   run_id: Text,
                                   pat: Text):
        func_id = 3

        suffix_check = self.df.where(
            column + rf" rlike r'(^|,|-|\.|.* )((J|S)N?R|(JU|SE)NIOR|M(D|R|S)|DR|I{2,}(V|X)?|I+(V|X)|(V|X)(I+)|PT)( .*|,|-|\.|$)|.* (I|V|X)\.?$'").count()
        df_suffix_check = source_data.where(
            column + rf" rlike r'(^|,|-|\.|.* )((J|S)N?R|(JU|SE)NIOR|M(D|R|S)|DR|I{2,}(V|X)?|I+(V|X)|(V|X)(I+)|PT)( .*|,|-|\.|$)|.* (I|V|X)\.?$'")

        # print('value of check3: ', suffix_check)
        self.check_store_result(func_id, suffix_check, source_data, column)

    # ZIP Validation----------------------------------------------------------------------------------------------------
    def check_func_zip(self,
                       source_data: DataFrame,
                       column: Text,
                       run_id: Text,
                       pat: Text):

        global zip_check
        func_id = 4
        m = re.match(pat, column)
        if m:
            name_type = m.group(1)
            if name_type == 'code4' or name_type == 'zip4':
                zip_check = source_data.where(((length(col(column)) > 4) & (length(col(column)) != 0)) | (
                        (length(col(column)) < 4) & (length(col(column)) != 0))).count()
                df_zip_check = source_data.where(((length(col(column)) > 4) & (length(col(column)) != 0)) | (
                        (length(col(column)) < 4) & (length(col(column)) != 0)))
            else:
                zip_check = self.df.where(((length(col(column)) > 5) & (length(col(column)) != 0)) | (
                        (length(col(column)) < 5) & (length(col(column)) != 0))).count()
                df_zip_check = self.df.where(((length(col(column)) > 5) & (length(col(column)) != 0)) | (
                        (length(col(column)) < 5) & (length(col(column)) != 0)))

        print(f'value of zip check for col {column} is  {zip_check}')
        self.check_store_result(func_id, zip_check, source_data, column)

    def check_batchID(self,
                      source_data: DataFrame,
                      column: Text,
                      run_id: Text,
                      pat: Text):
        func_id = 5
        BID_check = self.df.where(((length(col(column)) > 6) & (length(col(column)) != 0)) | (
                (length(col(column)) < 6) & (length(col(column)) != 0))).count()

        self.check_store_result(func_id, BID_check, source_data, column)

    def check_state(self,
                    source_data: DataFrame,
                    column: Text,
                    run_id: Text,
                    pat: Text):
        func_id = 6
        state_check = self.df.where(((length(col(column)) > 2) & (length(col(column)) != 0)) | (
                (length(col(column)) < 2) & (length(col(column)) != 0))).count()

        self.check_store_result(func_id, state_check, source_data, column)

    def check_gender(self,
                     source_data: DataFrame,
                     column: Text,
                     run_id: Text,
                     pat: Text):
        func_id = 7
        gender_check = self.df.where(f"NOT({column} IS NULL OR {column} RLIKE r'[MFUO]')").count()
        self.check_store_result(func_id, gender_check, source_data, column)

    def check_dob(self,
                  source_data: DataFrame,
                  column: Text,
                  run_id: Text,
                  pat: Text):
        func_id = 8
        dob_check = self.df.where(((length(col(column)) > 6) & (length(col(column)) != 0)) | (
                (length(col(column)) < 6) & (length(col(column)) != 0))).count()
        self.check_store_result(func_id, dob_check, source_data, column)

    def check_space(self,
                    df: DataFrame,
                    column: Text,
                    run_id: Text,
                    pat: Text):
        global space_check
        func_id = 9
        space_check = self.df.filter(col(f"{column}").rlike("^\\s|\\s$")).count()
        #df_space_check = self.df.filter(col(f"{column}").rlike("^\\s|\\s$"))

        print('value of space_check: ', space_check)
        #print('\nvalue of df_space_check: ', df_space_check)
        self.check_store_result(func_id, space_check, df, column)

    def check_cleanup(self,
                    df: DataFrame,
                    column: Text,
                    run_id: Text,
                    pat: Text):
        global cleanup_check_count
        func_id = 10
        cleanup_check_count = self.df.filter(col(f"{column}").rlike("^\\s|\\s$|\\s{2,}")).count()

        print('Number of missing cleanups:', cleanup_check_count)
        self.check_store_result(func_id, cleanup_check_count, df, column)

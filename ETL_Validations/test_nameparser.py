import os
import tempfile
from pathlib import Path
from typing import Text

import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="module")
def spark() -> SparkSession:
    builder = SparkSession.builder \
        .appName('we_pipeline_test') \
        .config('spark.ui.showConsoleProgress', 'false') \
        .config('spark.sql.debug.maxToStringFields', '200')

    if 'SPARK_MASTER' in os.environ:
        builder = builder.master(os.environ['SPARK_MASTER'])
    else:
        builder = builder.master('local[1]')

    s = builder.getOrCreate()

    with tempfile.TemporaryDirectory("we_pipeline") as dir:
        s.sparkContext.setCheckpointDir(dir)
        yield s
        s.stop()

    """
    # local checkpoint dir testing
    s.sparkContext.setCheckpointDir("./checkpoint")
    yield s
    s.stop()
    """


@pytest.fixture(scope="module")
def config_file() -> Text:
    file = "we/pipeline/core/config/we_pipeline_config_test.json"
    return (Path(os.getcwd()) / file).as_posix()


from we.pipeline.core.transformation.name_parser_lib import *
from chispa import (
    assert_df_equality,
    assert_column_equality)

from pyspark.sql.functions import monotonically_increasing_id
import pytest

########################
# Reference data lists
########################

_TITLE_LIST = ['PHD', 'MBA', 'MD', 'MPH', 'DSC']
_SUFFIX_LIST = ['JR', 'SR', 'II', 'III', 'IV', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV',
                'XVI', 'XVII', 'XVIII', 'XIX', 'XX', '2ND', '3RD', '4TH', '5TH']
_PREFIX_CONCATENATED_LIST = ['DE LA', 'DEL LA', 'DEL LE', 'DEL LI', 'DEL LO', 'VAN DER', 'VON DER', 'VON DEM',
                             'VAN DEN', 'VAN DE']
_PREFIX_LIST = ['BON', 'DA', 'DAL', 'DE', 'DEGLI', 'DEI', 'DEL', 'DELA', 'DELLA', 'DELLE', 'DELLI', 'DELLO', 'DER',
                'DI', 'DOS', 'DU', 'LA', 'LE', 'MAC', 'MC', 'SAN', 'SANTA', 'ST', 'STE', 'VAN', 'VANDER', 'VONDER',
                'VONDEM', 'VANDEN', 'VANDE', 'VEL', 'VON', 'VOM']


class TestNameParser():

    ####################################
    # function to run a unit test
    ####################################

    @staticmethod
    def run_unit_test(spark, func_name, data, lists):
        '''
        Function to run a unit test and display test results.
            Arguments:
            spark: SparkSession object

            func_name: name of the function to be tested.

            data: an array of tuples or lists, each element having input and expected output

            lists: dictionary of input,output and expected

            column names list for the function in context

        '''
        # get the lists from the dictionary

        output_col_list = lists["output"]
        inpt_col_list = lists["input"]
        expected_output_list = lists["expected"]

        # Creating the input dataframe
        df = spark.createDataFrame(data, [*(inpt_col_list), *(expected_output_list)])

        f_name = str(func_name).split(" ")[1]

        index = 0
        for output_col in output_col_list:
            if output_col in inpt_col_list:
                # copying input data in column named input_ to address in-place transformations
                index = inpt_col_list.index(output_col)

        if f_name == NameParser.perform_name_transformations_and_standardization:
            index = 0

        input_col = "input_" + inpt_col_list[index]
        df = df.withColumn(input_col, col(inpt_col_list[index]))
        inpt_col_list.pop(index)
        inpt_col_list.append(input_col)

        print(inpt_col_list)

        # generating serial number SN
        df = df.select("*").withColumn("SN", monotonically_increasing_id())

        if f_name in ("NameParser.process", "NameParser.perform_name_cleansing",
                      "NameParser.perform_name_transformations_and_standardization"
                      ):
            df = func_name(NameParser(["owner__src_full_name"]), df)

        elif (f_name == "NameParser.digits_and_hypen_betwn_digits_removal"):
            df = func_name(df, "owner__src_full_name")

        else:
            df = func_name(df)

        # reordering the columns
        if str(func_name).split(" ")[1] == "NameParser.populate_all_std_col_attr_in_camelcase":
            select_exprs = [col('SN')] + [col(col_name) for col_name in expected_output_list] \
                           + [col(col_name) for col_name in output_col_list]
        else:
            select_exprs = [col('SN')] + [col(col_name) for col_name in inpt_col_list] \
                           + [col(col_name) for col_name in expected_output_list] \
                           + [col(col_name) for col_name in output_col_list]

        df = df.select(*select_exprs)

        # Display TEST REPORT

        print(f"TEST RESULTS FOR FUNCTION: {func_name}")
        # pd.set_option('display.max_colwidth', 80)
        # result_df.toPandas()
        df.show(25, False)

        # Assert expected with actual

        for i in range(0, len(lists["output"])):
            """ assert_column_equality function from the chispa library.
            which will help to test the column equality at dataframe level."""
            assert_column_equality(df, lists["expected"][i], lists["output"][i])

    ########################################
    # UNIT TESTS FOR NAME PARSER
    #######################################

    # Test1
    @staticmethod
    @pytest.mark.xfail
    def test_digits_and_hypen_betwn_digits_removal(spark):
        func_name = NameParser.digits_and_hypen_betwn_digits_removal

        data = [("GOLDWYN ELIZABETH 1986", "GOLDWYN ELIZABETH"),
                ("GOLDWYN ELIZABETH 1 9 86", "GOLDWYN ELIZABETH"),
                ("GOLDWYN 1234 ELIZABETH", "GOLDWYN ELIZABETH"),
                ("GOLDWYN 1234 ELIZABETH 4567", "GOLDWYN ELIZABETH"),
                ("1234 GOLDWYN ELIZABETH", "GOLDWYN ELIZABETH"),
                ("RYDING NEIL 122-62-507", "RYDING NEIL"),
                ("RYDING NEIL 122-62-", "RYDING NEIL"),
                ("RYDING NEIL 122-", "RYDING NEIL"),
                ("122-62-507 RYDING NEIL", "RYDING NEIL"),
                ("RYDING 122-62-507 NEIL", "RYDING NEIL"),
                ("RYDING-NEIL", "RYDING-NEIL"),
                ("SUSAN CLARK TWINING TRUST1946", "SUSAN CLARK TWINING TRUST1946"),
                ("SUSAN CLARK TWINING1946 TRUST", "SUSAN CLARK TWINING1946 TRUST"),
                ("SUSAN CLARK1946 TWINING TRUST", "SUSAN CLARK1946 TWINING TRUST"),
                ("SUSAN0876 CLARK TWINING TRUST", "SUSAN0876 CLARK TWINING TRUST"),
                ("TWINING TRUST194-6", "TWINING TRUST1946"),
                ("SUSAN CLARK3RD-6", "SUSAN CLARK3RD-6"),
                ("SUSAN0876CLARK", "SUSAN0876CLARK"),
                ]
        lists = {}
        lists["input"] = ["owner__src_full_name"]
        lists["output"] = ['cleansed_src_full_name']
        lists['expected'] = ['expected_result']
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test2
    @staticmethod
    def test_replace_comma_and_double_quotes_with_space(spark):
        func_name = NameParser.replace_comma_and_double_quotes_with_space
        data = [
            ('"WILLIAM C FRANCE FAMILY TRUST DATED NOVEMBER 4, 2004"',
             "WILLIAM C FRANCE FAMILY TRUST DATED NOVEMBER 4  2004"),
            ('"WILLIAM" "C ,FRANCE", FAMILY TRUST "DATED NOVEMBER 4, 2004',
             "WILLIAM   C  FRANCE   FAMILY TRUST  DATED NOVEMBER 4  2004"),
            ('"""TRUST FBO JAMES WAGNER ALTSCHUL""", U/A/D 08/20/1998""',
             "TRUST FBO JAMES WAGNER ALTSCHUL     U/A/D 08/20/1998")
        ]
        lists = {}
        lists["input"] = ["cleansed_src_full_name"]
        lists["output"] = ["cleansed_src_full_name_v2"]
        lists["expected"] = ["expected"]
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test3

    @staticmethod
    def test_remove_words_within_with_parenthesis(spark):

        data = [
            ('KEVIN T PARKER FAMILY TRUST (2007)', 'KEVIN T PARKER FAMILY TRUST'),
            ('KEVIN T PARKER FAMILY (TRUST 2007)', 'KEVIN T PARKER FAMILY'),
            ('KEVIN T PARKER (FAMILY TRUST 2007)', 'KEVIN T PARKER'),
            ('KEVIN T (PARKER FAMILY TRUST 2007)', 'KEVIN T'),
            ('KEVIN (T PARKER FAMILY TRUST 2007)', 'KEVIN'),
            ('(KEVIN T PARKER FAMILY TRUST 2007)', ''),
            ('KEVIN (T) PARKER FAMILY TRUST 2007', 'KEVIN  PARKER FAMILY TRUST 2007'),
            ('KEVIN (-$&@*%+!~786) PARKER FAMILY TRUST', 'KEVIN  PARKER FAMILY TRUST'),
            ('KEVIN T PARKER FAMILY TRUST ()', 'KEVIN T PARKER FAMILY TRUST'),
            ('()KEVIN T PARKER FAMILY TRUST (2007)', 'KEVIN T PARKER FAMILY TRUST')
        ]
        func_name = NameParser.remove_words_within_with_parenthesis
        lists = {}
        lists["input"] = ["cleansed_src_full_name_v2"]
        lists["output"] = ["cleansed_src_full_name_v2"]
        lists["expected"] = ["expected"]
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test4
    @staticmethod
    def test_remove_chars_after_slash(spark):
        func_name = NameParser.remove_chars_after_slash
        data = [
            ("YOUNG A THOMAS/CA", "YOUNG A THOMAS"),
            ("JOHNSON JAMES A /DC/", "JOHNSON JAMES A"),
            ("DAVIS MICHAEL A /", "DAVIS MICHAEL A"),
            ("KNOWLES MARIE L/CA", "KNOWLES MARIE L"),
            ("KNOWLES MARIE L/ CA", "KNOWLES MARIE L"),
            ("KNOWLES/123 MARIE L", "KNOWLES"),
            ("KNOWLES MARIE/@%*/ L", "KNOWLES MARIE"),
            ("/KNOWLES MARIE L", ""),
            ("PARDO JAIME CHICO /FA", "PARDO JAIME CHICO"),
            ("TRUST FBO ARTHUR G ALTSCHUL JR UAD 11/20/64", "TRUST FBO ARTHUR G ALTSCHUL JR UAD 11"),
            ("HAGGERTY TERRY LEE                                      /BD", \
             "HAGGERTY TERRY LEE"),
            ("WILLIAM N HARWIN 2012 GIFT TRUST F/B/O PETER HARWIN", "WILLIAM N HARWIN 2012 GIFT TRUST F"),
            ("CHLOE R SEELBACH, TRUSTEE UNDER CLAIBORNE RANKIN TRUST FOR CHILDREN OF CHLOE R SEELBACH DTD 12/21/04", \
             "CHLOE R SEELBACH, TRUSTEE UNDER CLAIBORNE RANKIN TRUST FOR CHILDREN OF CHLOE R SEELBACH DTD 12"),
            ("SHELDON G ADELSON 2005 FAMILY TRUST U/D/T DATED APRIL 25, 2005", \
             "SHELDON G ADELSON 2005 FAMILY TRUST U")
        ]
        lists = {}
        lists["input"] = ["cleansed_src_full_name_v2"]
        lists["output"] = ["cleansed_src_full_name_v2"]
        lists["expected"] = ["expected"]
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    ##Test5
    @staticmethod
    def test_take_char_with_max_length_after_split_with_ampersand(spark):
        func_name = NameParser.take_char_with_max_length_after_split_with_ampersand
        data = [
            ("CALLON LEEANNA & FRED", "CALLON LEEANNA"),
            ("SIMONS &", "SIMONS"),
            ("J&M", "J&M"),
            ("LEON & TOBY COOPERMAN FOUNDATION", "TOBY COOPERMAN FOUNDATION"),
            ("& R MCADAMS JR", "R MCADAMS JR"),
            ("123&456", "123&456")
        ]

        lists = {}
        lists["input"] = ["cleansed_src_full_name_v2"]
        lists["output"] = ["cleansed_src_full_name_v2"]
        lists["expected"] = ["expected"]
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test6
    @staticmethod
    def test_optional_cleansing_process(spark):
        func_name = NameParser.optional_cleansing_process
        data = [
            ("AMER VALUES BERMUD", "AMER VALUES (IV) BERMUD", "AMER VALUES BERMUD IV"),
            ("AMER VALUES BERMUD", "AMER(iv) VALUES BERMUD", "AMER VALUES BERMUD IV"),
            ("AMER VALUES BERMUD", "(iv) AMER VALUES BERMUD", "AMER VALUES BERMUD IV"),
        ]

        lists = {}
        lists["input"] = ["cleansed_src_full_name_v2", "cleansed_src_full_name"]
        lists["output"] = ["cleansed_src_full_name_v2"]
        lists["expected"] = ["expected"]
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test7

    @staticmethod
    def test_replace_mutiple_space_with_single_space(spark):
        func_name = NameParser.replace_mutiple_space_with_single_space
        data = [("ABC  D", "ABC D"),
                ("AB   CD", "AB CD"),
                ("A    BCD", "A BCD")
                ]
        lists = {}
        lists["input"] = ["cleansed_src_full_name_v2"]
        lists["output"] = ["cleansed_src_full_name_v2"]
        lists["expected"] = ["expected"]
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test8
    @staticmethod
    def test_generate_name_array_by_split_with_space(spark):
        func_name = NameParser.generate_name_array_by_split_with_space
        data = [("Shalini XVI Agarwal", ['SHALINI', 'XVI', 'AGARWAL']),
                ("Coded by iv Dev phd", ['CODED', 'BY', 'IV', 'DEV', 'PHD']),
                ("2nd Testing is done by QA", ['2ND', 'TESTING', 'IS', 'DONE', 'BY', 'QA'])]

        lists = {}
        lists["input"] = ["cleansed_src_full_name_v2"]
        lists["output"] = ["cleansed_src_full_name_arr"]
        lists["expected"] = ["expected"]
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test9
    @staticmethod
    def test_add_titles_suffixes_array_attr(spark):
        func_name = NameParser.add_titles_suffixes_array_attr

        data = [("abc", _TITLE_LIST, _SUFFIX_LIST)]
        print(data)

        lists = {}
        lists["input"] = ["dummy"]
        lists["output"] = ["titles", "suffixes"]
        lists["expected"] = ["expected_titles", "expected_suffixes"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test10
    @staticmethod
    def test_find_matching_title_suffix_between_arr(spark):

        func_name = NameParser.find_matching_title_suffix_between_arr

        data = [(['PHD', 'Shalini', 'AgarwalJR', 'T'], _TITLE_LIST, _SUFFIX_LIST, ['PHD'], []),
                (['MBAShalini', 'Agarwal', 'SR'], _TITLE_LIST, _SUFFIX_LIST, [], ['SR']),
                (['J', 'P', 'MPH', 'Morgan)', 'II', 'Stanley'], _TITLE_LIST, _SUFFIX_LIST, ['MPH'], ['II']),
                (['Shalini', 'IIMPH', 'Agarwal'], _TITLE_LIST, _SUFFIX_LIST, [], []),
                (['Shalini', 'MD', 'Agarwal'], _TITLE_LIST, _SUFFIX_LIST, ['MD'], []),
                (['Shalini', 'Agarwal', '4TH', '5TH'], _TITLE_LIST, _SUFFIX_LIST, [], ['4TH', '5TH']),
                (['Shalini', '2ND', 'Agarwal'], _TITLE_LIST, _SUFFIX_LIST, [], ['2ND']),
                (['Shalini', 'Agarwal', '2ND3RD'], _TITLE_LIST, _SUFFIX_LIST, [], []),
                (['DSCPHD', 'Shalini', 'Agarwal'], _TITLE_LIST, _SUFFIX_LIST, [], []),
                (['DSC', 'PHD', 'Shalini', 'Agarwal'], _TITLE_LIST, _SUFFIX_LIST, ['DSC', 'PHD'], []),
                (['P', 'V', 'DSC', 'Narasimha', 'VI', 'Rao'], _TITLE_LIST, _SUFFIX_LIST, ['DSC'], ['VI']),
                (['BILL', 'XIV', 'GATES'], _TITLE_LIST, _SUFFIX_LIST, [], ['XIV']),
                (['Lower', 'case', 'suffix', 'iv'], _TITLE_LIST, _SUFFIX_LIST, [], []),
                (['mph', 'Lower', 'case', 'title'], _TITLE_LIST, _SUFFIX_LIST, [], []),
                (['mba', 'both', ' in ', 'xx', 'lower', 'case', 'Xi'], _TITLE_LIST, _SUFFIX_LIST, [], [])
                ]

        lists = {}
        lists["input"] = ["cleansed_src_full_name_arr", "titles", "suffixes"]
        lists["output"] = ["matched_title", "matched_suffix"]
        lists["expected"] = ["expected_matched_title", "expected_matched_suffix"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test11

    @staticmethod
    def test_remove_title_suffix_from_name_arr(spark):

        func_name = NameParser.remove_title_suffix_from_name_arr
        data = [
            (['PHD', 'Shalini', 'AgarwalJR'], ['PHD'], [], ['Shalini', 'AgarwalJR']),
            (['MBAShalini', 'Agarwal', 'SR'], [], ['SR'], ['MBAShalini', 'Agarwal']),
            (['J', 'P', 'MPH', 'MORGAN', 'II', 'STANLEY'], ['MPH'], ['II'], ['J', 'P', 'MORGAN', 'STANLEY']),
            (['Shalini', 'IIMPH', 'Agarwal'], [], [], ['Shalini', 'IIMPH', 'Agarwal']),
            (['Shalini', 'MD', 'Agarwal'], ['MD'], [], ['Shalini', 'Agarwal']),
            (['Shalini', 'Agarwal', '4TH', '5TH'], [], ['4TH', '5TH'], ['Shalini', 'Agarwal']),
            (['Shalini', 'Agarwal', '2ND3RD'], [], [], ['Shalini', 'Agarwal', '2ND3RD']),
            (['DSCPHD', 'Shalini', 'Agarwal'], [], [], ['DSCPHD', 'Shalini', 'Agarwal']),
            (['DSC', 'PHD', 'Shalini', 'Agarwal'], ['DSC', 'PHD'], [], ['Shalini', 'Agarwal']),
            (['P', 'V', 'DSC', 'Narasimha', 'VI', 'Rao'], ['DSC'], ['VI'], ['P', 'V', 'Narasimha', 'Rao']),
            (['BILL', 'XIV', 'GATES'], [], ['XIV'], ['BILL', 'GATES']),

        ]

        lists = {}
        lists["input"] = ["cleansed_src_full_name_arr", "matched_title", "matched_suffix"]
        lists["output"] = ["cleansed_src_full_name_arr"]
        lists["expected"] = ["expected_result"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test12

    @staticmethod
    def test_add_and_remove_matched_concat_prefix_from_name_arr(spark):
        func_name = NameParser.add_and_remove_matched_concat_prefix_from_name_arr
        data = [
            (['DEL', 'Ratan', 'LO', 'tata'], ['DEL', 'Ratan', 'LO', 'tata']),
            (['VAN', 'DER', 'H.J.', 'Bhabha'], ['H.J.', 'Bhabha']),
            (['B.', 'VON', 'DER', 'R.', 'Ambedkar'], ['B.', 'VON', 'DER', 'R.', 'Ambedkar']),
            (['VONDEM', 'Mukesh', 'Ambani'], ['VONDEM', 'Mukesh', 'Ambani'])
        ]
        lists = {}
        lists["input"] = ["cleansed_src_full_name_arr"]
        lists["output"] = ["cleansed_src_full_name_arr"]
        lists["expected"] = ["expected_result"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test13
    @staticmethod
    def test_add_and_remove_matched_prefix_from_name_arr(spark):
        data = [(['BON', 'Shalini', 'Agarwal'], ['Shalini', 'Agarwal']),
                (['shalini', 'DEGLI', 'Agarwal'], ['shalini', 'DEGLI', 'Agarwal']),
                (['Shalini', 'Agarwal', 'SANTA'], ['Shalini', 'Agarwal', 'SANTA']),
                (['LA', 'H', 'J', 'Bhabha'], ['H', 'J', 'Bhabha']),
                (['VOM', 'J', 'R', 'D', 'Tata'], ['J', 'R', 'D', 'Tata'])
                ]
        func_name = NameParser.add_and_remove_matched_prefix_from_name_arr
        lists = {}
        lists["input"] = ["cleansed_src_full_name_arr"]
        lists["output"] = ["cleansed_src_full_name_arr"]
        lists["expected"] = ["expected_result"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test14

    @staticmethod
    def test_get_size_of_transformed_name_arr(spark):
        func_name = NameParser.get_size_of_transformed_name_arr
        data = [(["Peter"], 1),
                (["Shalini", "Agarwal"], 2),
                (["H", "J", "Bhabha"], 3),
                (["J", "R", "D", "Tata"], 4)]

        lists = {}
        lists["input"] = ["cleansed_src_full_name_arr"]
        lists["output"] = ["cleansed_src_full_name_arr_size"]
        lists["expected"] = ["expected_result"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test15
    @staticmethod
    def test_add_prefix_col_attr(spark):
        func_name = NameParser.add_prefix_col_attr
        data = [('VAN DEN', 'SANTA', None),
                (None, 'VONDEM', "VONDEM"),
                ('DEL LE', None, "DEL LE"),
                (None, None, None)]
        lists = {}

        lists["input"] = ["matched_concatenated_prefix", "matched_prefix"]
        lists["output"] = ["prefix"]
        lists["expected"] = ["expected_result"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test16
    @staticmethod
    def test_populate_all_std_col_attr_in_camelcase(spark):
        func_name = NameParser.populate_all_std_col_attr_in_camelcase

        data = [('SAN', ['LAST', 'FIRST', 'MIDDLE'], 3, ["5TH"], _SUFFIX_LIST, 'First', 'Middle', 'San Last', '5th',
                 'First Middle San Last 5th'),
                (None, ["H", "J", "BHABHA"], 3, ["XIV"], _SUFFIX_LIST, "J", "Bhabha", "H", "XIV", "J Bhabha H XIV"),
                ('VANDEN', ["TATA", "J", "R", "D"], 4, [], _SUFFIX_LIST, "J", "R", "Vanden Tata", None,
                 "J R Vanden Tata"),
                ('MC', ["AGARWAL", "SHALINI"], 2, ["JR"], _SUFFIX_LIST, 'Shalini', None, 'Mc Agarwal', 'Jr',
                 'Shalini Mc Agarwal Jr'),
                ('DEL LE', ["PETER "], 1, ["2ND"], _SUFFIX_LIST, None, None, 'Del Le Peter', '2nd', 'Del Le Peter 2nd')]

        lists = {}
        lists["input"] = ["prefix", "cleansed_src_full_name_arr", "cleansed_src_full_name_arr_size", "matched_suffix",
                          "suffixes"]
        lists["output"] = ["owner__std_first_name", "owner__std_middle_name", "owner__std_last_name",
                           "owner__std_suffix",
                           "owner__std_full_name"]
        lists["expected"] = ["expected_first_name", "expected_middle_name", "expected_last_name", 'expected_suffix',
                             "expected_full_name"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test17
    @staticmethod
    def test_drop_unwanted_cols(spark):
        func_name = NameParser.drop_unwanted_cols
        data = [("testfield", "ABCD", ["ABCD"], "A", "B", 1, 2, ["titles"], ["suffixes"], ["m_titles"], ["m_suffix"],
                 ["m_prefix"], ["m_c_prefix"], 2, 'PHD')]
        col_name_list = ["test_field", "cleansed_src_full_name_v2", "cleansed_src_full_name_arr", "left_chars",
                         "right_chars",
                         "left_chars_length",
                         "right_chars_length", "titles", "suffixes", "matched_title", "matched_suffix",
                         "matched_concatenated_prefix",
                         "matched_prefix", "cleansed_src_full_name_arr_size", "prefix"]

        df = spark.createDataFrame(data, col_name_list)

        result_df = func_name(df)
        data1 = [("testfield",)]
        empty_df = spark.createDataFrame(data1, ["test_field"])
        print(f"Test results for {func_name}")
        print(f"Expected schema: {empty_df.schema},Returned_schema:,{result_df.schema}")

        assert (empty_df.schema == result_df.schema)

    # Test18
    @staticmethod
    def test_remove_space_before_and_after_hyphen(spark):
        func_name = NameParser.remove_space_before_and_after_hyphen
        data = [
            ("HAUB KARL- ERIVAN WARDER", "HAUB KARL-ERIVAN WARDER"),
            ("MACNIVEN -YOUNG MARILYN U", "MACNIVEN-YOUNG MARILYN U"),
            ("MUHLNER - WELLER KRISTIN", "MUHLNER-WELLER KRISTIN"),
            ("122-62- RYDING NEIL", "122-62-RYDING NEIL"),
            ("122- RYDING NEIL", "122-RYDING NEIL"),
            ("- RYDING NEIL", "-RYDING NEIL"),
            ("-RYDING NEIL", "-RYDING NEIL"),
            ("RYDING 122-62- NEIL", "RYDING 122-62-NEIL"),
            ("RYDING 122- NEIL", "RYDING 122-NEIL"),
            ("RYDING - NEIL", "RYDING-NEIL"),
        ]

        lists = {}

        lists["input"] = ["cleansed_src_full_name_v2"]
        lists["output"] = ["cleansed_src_full_name_v2"]
        lists["expected"] = ["expected_result"]
        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test19
    @staticmethod
    def test_perform_name_cleansing(spark):
        func_name = NameParser.perform_name_cleansing
        data = [("PHD Shalini Agarwal Sr", ['PHD', 'SHALINI', 'AGARWAL', 'SR']),
                ('VAN 12 FRANKLIN"2nd" II', ['VAN', 'FRANKLIN', '2ND', 'II']),
                ('PHD Franklin Robert "2nd"&II', ['PHD', 'FRANKLIN', 'ROBERT', '2ND']),
                ('PHD- Franklin Robert"2nd"&II', ['PHD-FRANKLIN', 'ROBERT', '2ND']),
                ('Van Franklin"2nd" II', ['VAN', 'FRANKLIN', '2ND', 'II'])
                ]

        lists = {}

        lists["input"] = ["owner__src_full_name"]
        lists["output"] = ["cleansed_src_full_name_arr"]
        lists["expected"] = ["expected_result"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # Test20
    @staticmethod
    @pytest.mark.xfail
    def test_perform_name_transformations_and_standardization(spark):
        func_name = NameParser.perform_name_transformations_and_standardization
        data = [(["VAN", "FRANKLIN", "2ND"], None, None, "Van Franklin", "2nd", 'Van Franklin 2nd'),
                (["VAN", "FRANKLIN", "II", '2nd'], '2nd', None, "Van Franklin", "II", '2nd Van Franklin II'),
                (["PHD", "FRANKLIN", "ROBERT", "2ND"], "Franklin", None, "Robert", "2nd", 'Robert Franklin 2nd'),
                (["PHD-FRANK", " ROBERT", "2ND"], "Phd-Franklin", None, " Robert", "2nd", "Robert Phd-franklin 2nd"),
                (["J", "COX", "MBA"], "Cox", None, "J", None, "Cox J"),
                (["HENRY", "FORD", "BEN", "II"], "Ford", "Ben", "Henry", "II", "Ford Ben Henry II"),
                (["HENRY", "FORD", "J", "BEN", "4TH"], "Ford", "J", "Henry", "4th", "Ford J Henry 4th"),
                (["VAN", "FRANKLIN", "2ND", "II"], "VAN", "FRANKLIN", "2ND", "II", "Van Franklin 2nd II"),
                (["VAN", "FRANKLIN", "2nd", 'II'], 'II', None, "Van Franklin", "2nd", 'II Van Franklin 2nd')
                ]

        lists = {}

        lists["input"] = ["cleansed_src_full_name_arr"]
        lists["output"] = ["owner__std_first_name", "owner__std_middle_name", "owner__std_last_name",
                           "owner__std_suffix",
                           "owner__std_full_name"]
        lists["expected"] = ["expected_first_name", "expected_middle_name", "expected_last_name", 'expected_suffix',
                             "expected_full_name"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

    # test21

    @staticmethod
    @pytest.mark.xfail
    def test_process(spark):
        func_name = NameParser.process
        lists = {}

        data = [("Mac J   PHD-R VI D Tata  ", "Phd-r D Mac J VI"),
                ("J   PHD VI D Tata  ", "D Tata J VI"),
                ("(3rd,Jr) & MBA Nei'l/armstrong", "Nei'l"),
                ("&Peter-3rd, iv STE", "Ste Peter3rd IV"),
                ('Lastname, Firstname", "Middlename ', "Firstname Middlename Lastname"),
                (' PHD MBA "Lastname, Firstname", "Middlename ', "Firstname Middlename Lastname"),
                ('BON DOS "Lastname, Firstname", "Middlename ', 'Firstname Middlename Bon Dos Lastname'),
                ("TWINING TRUST194-6", "TWINING TRUST1946"),
                ("Name from “Word”", "Name from Word"),
                ("St. Nei'l/1 daniel xvi armstrong MPH", "Nei'l St XVI"),
                ('Van Franklin"2nd" II', 'Van Franklin 2nd'),
                ('PHD- Franklin Robert"2nd"&II', "Robert2nd Phd- Franklin II"),
                ('PHD Franklin Robert "2nd"&II', "Robert Franklin 2nd"),
                ('VAN 12 FRANKLIN"2nd" II', 'Van Franklin 2nd II'),
                ('GOLDWYN ELIZABETH 1986', 'Elizabeth Goldwyn'),
                ('BEARD STEPHEN W', 'Stephen W Beard'),
                ('XU HAOYING (WILSON)', 'Haoying Xu'),
                ('PETERSEN SIDNEY R/CA', 'Sidney R Petersen'),
                ('MURRAY RICHARD /CA/', 'Richard Murray'),
                ('AUGUST-DEWILDE KATHERINE', 'Katherine August-dewilde'),
                ('RIORDAN LEWIS &', 'Lewis Riordan'),
                ('YATES THOMAS &WAYNE', 'Thomas Yates'),
                ('PARKER & PARSLEY AQUISI', 'Aquisi Parsley'),
                ('& CB WOOD JR', 'Wood Cb Jr'),
                ('KLEINBERG KAPLAN WOLFF &', 'Kaplan Wolff Kleinberg')
                ]

        lists["input"] = ["owner__src_full_name"]
        lists["output"] = ["owner__std_full_name"]
        lists["expected"] = ["expected_result"]

        TestNameParser.run_unit_test(spark, func_name, data, lists)

        # if __name__ == '__main__':
        #     pytest.main()

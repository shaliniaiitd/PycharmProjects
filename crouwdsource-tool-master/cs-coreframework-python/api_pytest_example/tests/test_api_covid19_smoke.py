import json

import pytest

from framework.api.requests.base_api import RestRequest
from framework.api.response.response_parser import deserialize, JSONValidator, CSVValidator
from framework.api.response.response_validator import RestResponse
from framework.core.utils.logger_factory import LoggerFactory
from requests_toolbelt.utils import dump

logger = LoggerFactory.get_logger("TEST")

"""
    Sample Tests which demonstrates the examples of consuming the Request and Response wrapper methods 
"""


def test_get_validate_status_code_200(api_config):
    api_config.end_point = "data.json"
    response = RestRequest.get_raw_response(api_config)
    RestResponse.validate_status_code(response, 200)

# @pytest.mark.skip
def test_node_exists_in_response(api_config):
    api_config.end_point = "data.json"
    response = RestRequest.get_raw_response(api_config)
    response_data = deserialize(response, api_config.content_type)
    data = dump.dump_all(response)
    print(data.decode('utf-8'))
    JSONValidator.validate_node_in_response_body(response_data, "statewise")

# @pytest.mark.skip
def test_header_list_in_response(api_config, rp_logger):
    """
        Sample test method - CSV Parsing for response body.
        - rp_logger as a fixture for reporting console logs on Report Portal
    """
    rp_logger.info("Sample test method - CSV Parsing for response body")
    api_config.end_point = "csv/latest/state_wise.csv"
    response = RestRequest.get_raw_response(api_config)
    response_data = deserialize(response, "text/csv")
    CSVValidator.validate_header_list_in_response(response_data, ['State', 'Confirmed', 'Recovered', 'Deaths', 'Active', 'Last_Updated_Time',
                                                               'Migrated_Other', 'State_code', 'Delta_Confirmed', 'Delta_Recovered', 'Delta_Deaths', 'State_Notes'])

# @pytest.mark.skip
def test_node_jsonpath_in_response(api_config, rp_logger):
    """
        Sample test method - JSON Parsing for response body.
        - rp_logger as a fixture for reporting console logs on Report Portal
    """
    rp_logger.info("Sample test method - JSON Parsing for response body")
    api_config.end_point = "data.json"
    response = RestRequest.get_raw_response(api_config)
    response_data = deserialize(response, api_config.content_type)
    JSONValidator.validate_node_with_jsonpath_response(response_data, "$.statewise[2].deaths", "12452")


# @pytest.mark.skip
def test_node_list_in_response(api_config):
    response = RestRequest.get_raw_response(api_config)
    api_config.end_point = "data.json"
    response_data = deserialize(response, api_config.content_type)
    JSONValidator.validate_node_list_with_jsonpath_response(response_data, "$.statewise[*].deaths", ['383566', '17188', '2222'])


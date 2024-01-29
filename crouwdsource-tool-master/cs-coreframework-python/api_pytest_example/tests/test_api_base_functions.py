import pytest

from framework.api.requests.base_api import RestRequest
from framework.api.response.response_validator import RestResponse
"""
        Sample Tests which demonstrates the examples of consuming the Request and Response wrapper methods 
        Update qa.properties file and add entry as - 
        api.base.uri=http://regres.in
"""


def test_get_validate_status_code_200(api_config):
    api_config.end_point = "api/products/3"
    api_config.headers = {}
    response = RestRequest.requests_get(api_config)
    RestResponse.validate_status_code(response, 200)


def test_get_params_validate_status_code_200(api_config):
    api_config.end_point = "api/users"
    api_config.headers = {}
    api_config.params = {'page': '2'}
    response = RestRequest.requests_get(api_config)
    RestResponse.validate_status_code(response, 200)


def test_post_with_json_none_json_response(api_config):
    '''
    Method to test bad request i.e 400 status code which should not return any response
    '''
    api_config.end_point = "api123/users"
    api_config.headers = {'Content-Type': 'application/json'}
    request_data = '{"name": "morpheus1", "job": "leader1"}'
    response = RestRequest.requests_post(api_config, json_data=request_data)
    assert response.json_response is None


def test_post_neither_files_nor_data_given(api_config):
    api_config.end_point = "api/users"
    api_config.headers = {'Content-Type': 'application/json'}
    with pytest.raises(Exception, match="Provide atleast one argument data or json data or files"):
        RestRequest.requests_post(api_config)


def test_post_data_validate_status_code_201(api_config):
    api_config.end_point = "api/users"
    api_config.headers = {'Content-Type': 'application/json'}
    request_data = {'name': 'morpheus1', 'job': 'leader1'}
    response = RestRequest.requests_post(api_config, data=request_data)
    RestResponse.validate_status_code(response, 200)


def test_validate_protocol_version(api_config):
    api_config.end_point = "api/invalid/3"
    response = RestRequest.get_raw_response(api_config)
    RestResponse.validate_protocol_version(response, 11)


def test_validate_reason_phrase(api_config):
    api_config.end_point = "api/invalid/3"
    response = RestRequest.get_raw_response(api_config)
    RestResponse.validate_reason_phrase(response, "OK")

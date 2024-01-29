import json
from xml.etree import ElementTree
import csv
from jsonpath_ng import parse

from framework.core.utils.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger()

"""
    Response Parser Factory for returning either of below
        - JSON Data (Python Dictionary)
        - XML Data (Element Instance)
        - CSV Reader Object (Python List)
"""


def deserialize(response, content_type):
    deserialize_data = _get_parsed_data(content_type)
    return deserialize_data(response)


def _get_parsed_data(content_type):
    if content_type.lower() == 'application/json':
        return _json_parsed_data
    elif content_type.lower() == 'application/xml':
        return _xml_parsed_data
    elif content_type.lower() == 'text/csv':
        return _csv_parsed_data
    else:
        raise ValueError(f'Incorrect content type : {content_type} provided')


def _json_parsed_data(response):
    return json.loads(response.content)


def _xml_parsed_data(response):
    return ElementTree.fromstringlist(response.content)


def _csv_parsed_data(response):
    reader = csv.DictReader(response.text.splitlines(), delimiter=',')
    return list(reader)


class JSONValidator:
    """
        JSON Validator/Utility class to validate the json response body with expected json nodes/values
    """
    @staticmethod
    def validate_node_in_response_body(json_data, node, expected_value=None):
        if node in json_data:
            assert True
            if expected_value is not None:
                actual_value = json_data[node]
                assert actual_value == expected_value, f"Expected value for {node} is {expected_value} is not matching with actual value{actual_value}"
        else:
            assert False, f"{node} not exists"

    @staticmethod
    def validate_node_with_jsonpath_response(json_data, json_path, expected_value):
        json_path_expr = parse(json_path)
        match = json_path_expr.find(json_data)
        assert match[0].value == expected_value, f"Expected value {expected_value} does not match with actual value {match[0].value} "

    @staticmethod
    def validate_node_list_with_jsonpath_response(json_data, json_path, expected_list):
        json_path_expr = parse(json_path)
        match_list = json_path_expr.find(json_data)
        for match, item in zip(match_list, expected_list):
            assert match.value == item, f"Expected {item} does not match with actual value:{match.value}"

    @staticmethod
    def validate_if_node_does_not_exist(json_data, node):
        if node not in json_data:
            assert True
        else:
            assert False, f"{node} exists in given node"

    @staticmethod
    def get_child_nodes_from_parent_node(parent_node):
        nodes = []

        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], a)
                    nodes.append(a)
            elif type(x) is list:
                for a in x:
                    flatten(a, name)

        flatten(parent_node)
        return nodes

    @staticmethod
    def get_child_nodes_for_objects(objects):
        items = []
        nodes = json.loads(objects)
        for node in nodes:
            items.append(node)
        return items

    @staticmethod
    def validate_json(actual_json, expected_json):
        actual = json.loads(actual_json)
        expected = json.loads(expected_json)
        assert sorted(actual.items()) == sorted(expected.items()), "Given Jsons are not matching"


class CSVValidator:
    """
        CSV Validator/Utility class to validate the csv response body with expected json nodes/values
    """
    @staticmethod
    def validate_header_list_in_response(csv_data, expected_list):
        for match, item in zip(csv_data[0], expected_list):
            assert match == item, f"Expected {item} does not match with actual value:{match}"

    @staticmethod
    def validate_column_list_in_response(csv_data, column_header, expected_list):
        pass

    @staticmethod
    def validate_column_entry_in_response(csv_data, expected_column_value):
        pass

    @staticmethod
    def validate_row_entry_in_response(csv_data, expected_column_value):
        pass


class XMLValidator:
    """
        XML Validator/Utility class to validate the xml response body with expected json nodes/values
    """
    pass

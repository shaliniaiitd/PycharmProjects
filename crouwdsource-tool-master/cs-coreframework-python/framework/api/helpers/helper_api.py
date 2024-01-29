import json
from urllib.parse import urljoin

from requests.exceptions import MissingSchema

from framework.api.exceptions.user_defined_exceptions import InvalidURLException
from framework.core.utils.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger()


def build_url(config):
    """
    Builds url from APIConfiguration object and returns url
    :param config: config object to build url from its parameters
    :return: string(url)
    """
    url = ""
    logger.info(f"Base URL is set as : {config.base_url}")
    if config.base_url is None:
        raise MissingSchema
    elif not (config.base_url.startswith('http://') or (config.base_url.startswith('https://'))):
        print('Base URL is ', config.base_url)
        raise InvalidURLException
    else:
        url = urljoin(config.base_url, config.end_point)
        return url


def handle_http_error(response):
    """
    Builds and returns HTTP Error Message for 400 and 500 Status codes
    :param response :response object from requests
    :return : http error string
    """
    if 400 <= response.status_code < 500:
        http_error_msg = u'%s Client Error: %s for url: %s' % (response.status_code, response.reason, response.url)
    elif 500 <= response.status_code < 600:
        http_error_msg = u'%s Server Error: %s for url: %s' % (response.status_code, response.reason, response.url)
    else:
        http_error_msg = None
    return http_error_msg


def check_json_response(response):
    """
    Converts given json response to pretty json reposnse
    :param response : response object from requests
    :return : error message and json response
    """

    response_json = None
    pretty_json = None
    error_msg = None
    try:
        response_json = response.json()
        pretty_json = json.dumps(response.json(), separators=(",", ":"), indent=4)  # TBD needs to change the hard code
    except json.JSONDecodeError:
        error_msg = "json decode error"
    except Exception as ex:
        error_msg = "Unknown error"
    return error_msg, response_json


def rest_response_handle(response):
    """
    This Method handles http repsonse by checking the status code and building error message if needed
    or response if status is OK
    :params resposne :response object from requests
    :return :
        response: Http response object
        response.status_code: Http Status code
        response.text: response textr
        json_response: response json
        http_error_msg: http status code if status is 400 and 500
        json_error_msg: error message and json response
    """
    json_reponse = None
    http_error_msg = handle_http_error(response)
    json_error_msg, json_response = check_json_response(response)
    return response, response.status_code, response.text, json_response, http_error_msg, json_error_msg


def convert_to_json(data):
    """
    Converts given data to json format
    param data : a dictionary object
    returns : json string
    """
    try:
        json_string = json.dumps(data)
    except json.JSONDecodeError as jderror:
        raise Exception("Invalid JSON Format , Please check message body")
    return json_string


def files_to_upload(path):
    """
    builds a list of tuples each with file name and file descripter
    param path: list of file paths
    reurn : files
    """
    if not isinstance(path, (list, tuple)):
        path = [path]
    files = [('attachment', open(file, 'rb')) for file in path]
    return files


def validate_params(*args):
    """
    Checks args count, True only if any one of the args is not None.
    In all other cases it returns False
    :param args: params
    :return: boolean value or exception if invalid arg count
    """
    valid_args_count = sum([1 if arg else 0 for arg in args])
    if valid_args_count > 1:
        raise Exception("Provide only one paramater eith data or json data or files")
    elif valid_args_count == 0:
        raise Exception("Provide atleast one argument data or json data or files")
    else:
        return True

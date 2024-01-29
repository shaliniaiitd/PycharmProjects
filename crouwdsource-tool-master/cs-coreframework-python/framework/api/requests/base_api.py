'''
A wrapper around Requests to make RestFul API Calls
'''

import requests
from requests.exceptions import MissingSchema
from requests.structures import CaseInsensitiveDict
from framework.api.exceptions import user_defined_exceptions
from framework.api.helpers.helper_api import build_url, rest_response_handle, convert_to_json, files_to_upload, \
    validate_params
from framework.api.exceptions.user_defined_exceptions import InvalidURLException, InValidParam
from requests.auth import HTTPBasicAuth

from framework.api.response.response_validator import APIResponse
from framework.core.utils.logger_factory import LoggerFactory
from framework.core.utils.prop_file_reader import PropFileReader

PropFileReader.load_all_props()
logger = LoggerFactory.get_logger()


class APIConfiguration:
    TIME_OUT = 5
    """
    Building API configuration object will be used for API calls
    Attributes:
        base_url : base url
        end_point : relative url
        content_type : content type header in API call
        accept_type : accept type header in API call
        headers : headers for API call
        auth : auth for HTTP calls
        params : params for API call ,dictionary object
        allow_redirects : allow redirects on a HTTP call(default value is False).
        time_out : configurable timeout for API call
    """

    def __init__(self):
        self.base_url = None
        self.end_point = None
        self.content_type = None
        self.accept_type = None
        self.headers = {}
        self.auth = None
        self.params = None
        self.allow_redirects = False
        self.time_out = APIConfiguration.TIME_OUT  # TBD needs to be read from ini file

    def addHeader(self, key, value):
        self.headers = CaseInsensitiveDict()
        self.headers[key] = value

    def addAccept(self, value):
        self.headers = CaseInsensitiveDict()
        self.headers['Accept'] = value

    def addContentType(self, value):
        self.headers = CaseInsensitiveDict()
        self.headers['Content-Type'] = value

    def addBasicAuth(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    def addBearerTokenAuth(self, accessToken):
        self.headers = CaseInsensitiveDict()
        self.headers['Authorization'] = "Bearer {{ {0} }}".format(accessToken)

    def addNoCacheControlHeader(self, accessToken):
        self.headers = CaseInsensitiveDict()
        self.headers['cache-control'] = 'no-cache'

    def setErrorHandler(self, error_handler):
        pass


class RestRequest:
    @staticmethod
    def get_raw_response(config: APIConfiguration):
        url = build_url(config)
        try:
            response = requests.get(url=url,
                                    headers=config.headers,
                                    timeout=config.time_out,
                                    params=config.params,
                                    auth=config.auth)
            return response
        except requests.exceptions.MissingSchema as invalidURL:
            raise invalidURL
        except requests.exceptions.RequestException as excep:
            raise excep

    @staticmethod
    def requests_get(config: APIConfiguration):
        """
        Http Get request and returns APIResponse object
        Params config : APIConfiguration Object Example : httpbin.org/get?key=val
        return : APIResposne object
        """
        url = build_url(config)
        try:
            response = requests.get(url=url,
                                    headers=config.headers,
                                    timeout=config.time_out,
                                    params=config.params,
                                    auth=config.auth)
            response, status_code, text, json_response, http_err_msg, json_err_msg = rest_response_handle(response)
            return APIResponse(response, status_code, text, json_response, http_err_msg, json_err_msg)
        except requests.exceptions.RequestException as excep:
            # TBD:implement logger and update about exception
            raise excep

    @staticmethod
    def request_delete(config: APIConfiguration, data=None):
        """
        Http Delete request and returns APIResponse object
        Params config : APIConfiguration Object
        return : APIResposne object
        """
        url = build_url(config)
        try:
            if data != None:
                json_data = convert_to_json(data)
                response = requests.delete(url=url,
                                           headers=config.headers,
                                           params=config.params,
                                           data=json_data,
                                           timeout=config.time_out,
                                           auth=config.auth
                                           )
            else:
                response = requests.delete(url=url,
                                           headers=config.headers,
                                           timeout=config.time_out,
                                           auth=config.auth
                                           )

            response, status_code, text, json_response, http_err_msg, json_err_msg = rest_response_handle(response)
            return APIResponse(response, status_code, text, json_response, http_err_msg, json_err_msg)
        except requests.exceptions.RequestException as ex:
            # TBD:implement logger and update about exception
            raise ex

    @staticmethod
    def request_put(config: APIConfiguration, data=None, json_data=None, *files):
        """
        Http Put request and returns API response object
        Params
            config : APIConfiguration Object
            data : Message body
            json_data : josn data
            files : files path
        return : APIResposne object
        """
        response = None
        is_redirect = True
        url = build_url(config)
        try:
            while is_redirect:
                if data:
                    response = requests.put(url=url, params=config.params,
                                            data=convert_to_json(data),
                                            headers=config.headers,
                                            timeout=config.time_out,
                                            allow_redirects=config.allow_redirects,
                                            auth=config.auth)
                elif json_data:
                    response = requests.put(url=url, params=config.params,
                                            json=json_data,
                                            headers=config.headers,
                                            timeout=config.time_out,
                                            allow_redirects=config.allow_redirects,
                                            auth=config.auth)
                elif files:
                    file_list = files_to_upload(files)
                    response = requests.put(url=url, params=config.params,
                                            timeout=config.time_out,
                                            allow_redirects=config.allow_redirects,
                                            files=file_list,
                                            auth=config.auth)
                else:
                    raise user_defined_exceptions.ParamsMissing("Provide either data or json or file/s")
                is_redirect = response.is_redirect
                if is_redirect:
                    url = response.headers['Location']

            response, status_code, text, json_response, http_err_msg, json_err_msg = rest_response_handle(response)
            return APIResponse(response, status_code, text, json_response, http_err_msg, json_err_msg)
        except requests.exceptions.RequestException as ex:
            # TBD:implement logger and update about exception
            raise ex

    @staticmethod
    def requests_patch(config: APIConfiguration, data=None):
        """
        Http Patch call and returns API response object
        Params config : APIConfiguration Object
        data : message body
        return : APIResposne object
        """
        url = build_url(config)
        json_data = convert_to_json(data)
        try:
            response = requests.patch(url=url,
                                      params=config.params,
                                      data=json_data,
                                      headers=config.headers,
                                      timeout=config.time_out,
                                      auth=config.auth)
            response, status_code, text, json_response, http_err_msg, json_err_msg = rest_response_handle(response)
            return APIResponse(response, status_code, text, json_response, http_err_msg, json_err_msg)
        except requests.exceptions.RequestException as ex:
            # TBD:implement logger and update about exception
            raise ex

    @staticmethod
    def requests_post(config: APIConfiguration, data=None, json_data=None, files=None):
        """
        Http Post call and return API response object
        Params
        config : APIConfiguration Object
        data : message body
        json data : json data
        files : files paths
        return : APIResposne object
        """
        response = None
        is_redirect = True
        url = build_url(config)
        valid_params_count = validate_params(data, json_data, files)

        if valid_params_count:
            try:
                while is_redirect:
                    if data:
                        response = requests.post(url=url, params=config.params,
                                                 data=convert_to_json(data),
                                                 headers=config.headers,
                                                 timeout=config.time_out,
                                                 allow_redirects=config.allow_redirects,
                                                 auth=config.auth)
                    elif json_data:
                        response = requests.post(url=url, params=config.params,
                                                 json=json_data,
                                                 headers=config.headers,
                                                 timeout=config.time_out,
                                                 allow_redirects=config.allow_redirects,
                                                 auth=config.auth)
                    elif files:
                        file_list = files_to_upload(files)
                        response = requests.post(url=url, params=config.params,
                                                 timeout=config.time_out,
                                                 allow_redirects=config.allow_redirects,
                                                 files=file_list,
                                                 auth=config.auth)
                    else:
                        raise user_defined_exceptions.ParamsMissing("Provide either data or json or file/s")
                    is_redirect = response.is_redirect
                    if is_redirect:
                        url = response.headers['Location']
                response, status_code, text, json_response, http_err_msg, json_err_msg = rest_response_handle(response)
                return APIResponse(response, status_code, text, json_response, http_err_msg, json_err_msg)


            except requests.exceptions.RequestException as ex:
                # TBD:implement logger and update about exception
                raise ex

    @staticmethod
    def requests_clear_cookie(config: APIConfiguration):
        url = build_url(config)
        session = requests.session()
        session.get(url)
        session.cookies.clear()
        cookie_keys = session.cookies.keys()
        if cookie_keys is not None:
            return False
        else:
            return True

    @staticmethod
    def requests_update_cookie(config: APIConfiguration):
        url = build_url(config)
        session = requests.session()
        response = session.get(url=url, params=config.params)
        return response

    @staticmethod
    def requests_cookie_jar(config: APIConfiguration, cookie_key, cookie_value, url_path):
        url = build_url(config)
        jar = requests.cookies.RequestsCookieJar()
        jar.set(cookie_key, cookie_value, config.baseurl, url_path)
        response = requests.get(url=url, cookies=jar)
        response, status_code, text, json_response, http_err_msg, json_err_msg = rest_response_handle(response)
        return APIResponse(response, status_code, text, json_response, http_err_msg, json_err_msg)

    @staticmethod
    def remove_cookie(config, cookies):
        url = build_url(config)
        session = requests.session()
        session.get(url)
        cookie_keys = session.cookies.keys()
        if cookies in cookie_keys:
            session.cookies.pop(cookies)
        else:
            raise InValidParam(f"cookie {cookies} not existed.")

    @staticmethod
    def send_request_with_retry(statusCode, config, retryCount=1):
        for count in retryCount:
            response = RestRequest.requests_get(config)
            if statusCode == response.status_code:
                return response
            else:
                return False

    @staticmethod
    def validate_base_uri(config):
        if config.base_url is None:
            raise MissingSchema
        elif config.base_url.startswith('http://') or (config.base_url.startswith('https://')):
            raise InvalidURLException

    @staticmethod
    def add_body(config, body):
        RestRequest.requests_post(config, json_data=body)

    @staticmethod
    def add_body_as_form_data(config, data):
        RestRequest.requests_post(config, data=data)


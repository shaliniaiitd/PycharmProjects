
class APIResponse:
    '''
        API response object.
        Args:
            status_code : http status code
            text : text from response of api call
            json_response : json from response of api call
            error_msg : error message will be given for 4XX or 5XX response codes
                        else None
    '''

    def __init__(self, response, status_code, text, json_response, error_msg, json_error_msg):
        self.status_code = status_code
        self.text = text
        self.json_response = json_response
        self.http_error_msg = error_msg
        self.response = response
        self.json_error_msg = json_error_msg


class RestResponse:
    """
    REST Response Validator/Utility class for validation of -
        - Schema
        - Protocol Version
        - Reason Phrase
        - Status Code
        - Get Body
        - Get Status Code
    """

    @staticmethod
    def isSchemeHttp(response):
        return response.url.startswith("http:")

    @staticmethod
    def isSchemeHttps(response):
        return response.url.startswith("https:")

    @staticmethod
    def isSchemeNotHttp(response):
        return not response.url.startswith("http:")

    @staticmethod
    def isSchemeNotHttps(response):
        return not response.url.startswith("https:")

    @staticmethod
    def validate_protocol_version(response, expected_protocol_version):
        actual_protocol_version = response.raw.version
        assert actual_protocol_version == expected_protocol_version, f"Actual protocol version {actual_protocol_version} is not matching expected protocol version {expected_protocol_version}."

    @staticmethod
    def validate_reason_phrase(response, expected_reason_phrase):
        actual_reason_phrase = response.reason
        assert actual_reason_phrase == expected_reason_phrase, f"Actual Reason {actual_reason_phrase} is not matching with expected reason phrase: {expected_reason_phrase}."

    @staticmethod
    def validate_status_code(response, expected_status_code):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, f"Actual Status code {actual_status_code} is not matching with expected status code: {expected_status_code}."

    @staticmethod
    def get_status_code(response):
        return response.status_code

    @staticmethod
    def get_body(response):
        return response.content




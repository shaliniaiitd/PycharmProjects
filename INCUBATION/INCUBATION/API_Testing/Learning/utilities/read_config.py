import configparser


parser_obj = configparser.RawConfigParser()
parser_obj.read('../config/config.ini')

def get_url(url_name):
    return parser_obj.get('urls',url_name)


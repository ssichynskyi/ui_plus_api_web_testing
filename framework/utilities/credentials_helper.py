import os


class BasicAuthUser:
    def __init__(self, login, password):
        self.login = login
        self.password = password


class APIUser:
    def __init__(self, customer_key, customer_secret, token=None, token_secret=None):
        self.customer_key = customer_key
        self.customer_secret = customer_secret
        self.token = token
        self.token_secret = token_secret


normal_ui_user = BasicAuthUser(
    login=os.environ['STANDARD_USER_LOGIN'],
    password=os.environ['STANDARD_USER_PASSWORD']
)

woo_api_readonly_user = APIUser(
    customer_key=os.environ['WOO_API_READONLY_CONSUMER_KEY'],
    customer_secret=os.environ['WOO_API_READONLY_CONSUMER_SECRET']
)

woo_api_read_write_user = APIUser(
    customer_key=os.environ['WOO_API_READ_WRITE_CONSUMER_KEY'],
    customer_secret=os.environ['WOO_API_READ_WRITE_CONSUMER_SECRET']
)

wp_api_read_write_user = APIUser(
    customer_key=os.environ['WP_API_CONSUMER_KEY'],
    customer_secret=os.environ['WP_API_CONSUMER_SECRET'],
    token=os.environ['WP_API_TOKEN'],
    token_secret=os.environ['WP_API_TOKEN_SECRET']
)

db_user = BasicAuthUser(
    login=os.environ['DB_LOGIN'],
    password=os.environ['DB_PASSWORD']
)

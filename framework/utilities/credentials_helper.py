import os


class BasicAuthUser:
    def __init__(self, login, password):
        self.login = login
        self.password = password


class APIUser:
    def __init__(self, customer_key, customer_secret):
        self.customer_key = customer_key
        self.customer_secret = customer_secret


normal_ui_user = BasicAuthUser(
    login=os.environ['STANDARD_USER_LOGIN'],
    password=os.environ['STANDARD_USER_PASSWORD']
)

readonly_api_user = APIUser(
    customer_key=os.environ['READONLY_API_CONSUMER_KEY'],
    customer_secret=os.environ['READONLY_API_CONSUMER_SECRET']
)

read_write_api_user = APIUser(
    customer_key=os.environ['READ_WRITE_API_CONSUMER_KEY'],
    customer_secret=os.environ['READ_WRITE_API_CONSUMER_SECRET']
)

db_user = BasicAuthUser(
    login=os.environ['DB_LOGIN'],
    password=os.environ['DB_PASSWORD']
)

from rest_framework.exceptions import APIException

class InputExpectedException(APIException):
    status_code = 400
    default_detail = "Input body is expected"

    def __init__(self, detail):
        self.default_detail = detail + " body is expected"
        super(InputExpectedException, self).__init__()
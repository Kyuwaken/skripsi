from rest_framework.exceptions import APIException

class InputEmptyException(APIException):
    status_code = 400
    default_detail = "Input cannot be empty"

    def __init__(self, detail):
        self.default_detail = detail + " cannot be empty"
        super(InputEmptyException, self).__init__()
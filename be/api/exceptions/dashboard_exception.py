from rest_framework.exceptions import APIException


class DashboardException(APIException):
    status_code = 500
    default_detail = "Resource not found."

    def __init__(self, detail):
        self.default_detail = detail + " not found."
        super(DashboardException, self).__init__()

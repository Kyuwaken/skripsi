from api.exceptions import InputEmptyException,InputExpectedException, ValidationException

def validate_input(data,list_param):
    for param in list_param:
        if param not in data:
            raise InputExpectedException(param)
        if not data[param]:
            raise InputEmptyException(param)

def validate_integer(data,list_param):
    for param in list_param:
        if param not in data:
            raise InputExpectedException(param)
        try:
            tes = int(data[param])
        except:
            raise ValidationException('{} must be number'.format(param))
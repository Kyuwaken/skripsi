from threading import local
_thread_locals = local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

def set_current_user(user):
    _thread_locals.user = user

def get_current_request_log():
    return getattr(_thread_locals, 'request_log', None)


def set_current_request_log(request_log):
    _thread_locals.request_log = request_log
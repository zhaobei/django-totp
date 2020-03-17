import json
from functools import wraps

from django.http import HttpRequest, JsonResponse
from schema import Schema, SchemaError
from typing import Optional

from .exceptions import BaseException, InternalException


def api():
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except BaseException as e:
                return JsonResponse(dict(ret_code=e.ret_code, message=e.message, data=dict()))
            return JsonResponse(dict(ret_code=0, message='success', data=result))
        return wrapper
    return decorate


def _validate_request(request: HttpRequest, s: Schema):
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        raise BaseException(1, data=dict(err_msg='cannot json decode'))
    try:
        _body = s.validate(body)
    except SchemaError as e:
        raise BaseException(1, data=dict(err_msg=str(e)))
    setattr(request, '_body', _body)


def scm(s: Optional[Schema] = None):
    def decorate(func):
        @wraps(func)
        def wrapper(a, *args, **kwargs):
            if not s:
                pass
            if isinstance(a, HttpRequest):
                _validate_request(a, s)
            elif len(args) > 0 and isinstance(args[0], HttpRequest):
                _validate_request(args[0], s)
            else:
                raise InternalException('http request not found')
            return func(a, *args, **kwargs)
        return wrapper
    return decorate

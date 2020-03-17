from aop.api import api, scm

from schema import Schema
from aop.exceptions import InternalException

greet_schema = Schema(dict(id=int))


@api()
@scm(greet_schema)
def greet(request):
    return dict(hello='world')


@api()
def oops(request):
    raise InternalException('Oops!')

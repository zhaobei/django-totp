EXCEPTION_TABLE = (
    (0, 'success'),
    (1, 'invalid request body: {err_msg}'),
)
EXCEPTION_MESSAGE_MAP = {e[0]: e[1] for e in EXCEPTION_TABLE}


class BaseException(Exception):

    def __init__(self, ret_code, data={}, *args, **kwargs):
        self.ret_code = ret_code
        self.message = EXCEPTION_MESSAGE_MAP.get(self.ret_code, '').format(**data)
        return super().__init__(self.message, *args, **kwargs)


class InternalException(Exception):
    pass

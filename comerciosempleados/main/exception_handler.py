from rest_framework.response import Response
from rest_framework.views import exception_handler

from comerciosempleados.main.exceptions import BaseError


def custom_exception_handler(exc, context):
    if isinstance(exc, BaseError):
        data = {
            'rc': exc.rc,
            'msg': exc.msg,
        }
        response = Response(data)
    else:
        print(exc.__class__)
        old_response = exception_handler(exc, context)
        response = old_response
        # Now add the HTTP status code to the response.
        if response is not None:
            response.data['rc'] = response.status_code * -1
            response.data['msg'] = response.data['detail']
            del response.data['detail']

    if response is None:
        data = {
            'rc': -654,
            'msg': str(exc),
        }
        response = Response(data)

    return response

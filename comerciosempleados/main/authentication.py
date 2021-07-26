from uuid import UUID

from rest_framework import authentication, exceptions

from comerciosempleados.main.models import Comercio


class BasicAuthentication(authentication.BasicAuthentication):

    def authenticate_credentials(self, userid, password, request=None):
        try:
            api_key = UUID(userid)
        except ValueError:
            raise exceptions.AuthenticationFailed('API Key invalido')

        try:
            comercio = Comercio.objects.get(api_key=api_key, activo=True)
        except Comercio.DoesNotExist:
            raise exceptions.AuthenticationFailed('API Key invalida')

        return comercio, None

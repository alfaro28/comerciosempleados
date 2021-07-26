from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from comerciosempleados.main.authentication import BasicAuthentication
from comerciosempleados.main.exception_handler import custom_exception_handler
from comerciosempleados.main.exceptions import InvalidEmpleadoError, DuplicatedPinError, NoEmpleadoError, \
    IncompleteDataError
from comerciosempleados.main.json_renderer import JSONRenderer
from comerciosempleados.main.models import Empleado
from comerciosempleados.main.serializers import EmpleadoSerializer


class EmpleadosViews(APIView):
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    renderer_classes = [JSONRenderer, ]

    def get_exception_handler(self):
        return custom_exception_handler

    def get(self, request, *args, **kwargs):
        comercio = request.user
        uuid_empleado = kwargs.get('uuid_empleado', '')

        if uuid_empleado:
            try:
                empleado = comercio.empleados.get(uuid=uuid_empleado)
                serial = EmpleadoSerializer(empleado)
            except (Empleado.DoesNotExist, ValidationError):
                raise InvalidEmpleadoError()
        else:
            empleados = comercio.empleados.all()
            serial = EmpleadoSerializer(empleados, many=True)

        return Response(serial.data)

    def post(self, request, *args, **kwargs):
        comercio = request.user

        try:
            nombre = request.data["nombre"]
            apellidos = request.data["apellidos"]
            pin = request.data["pin"]
        except KeyError:
            raise IncompleteDataError()

        empleado = Empleado()
        empleado.nombre = nombre
        empleado.apellidos = apellidos
        empleado.pin = pin
        empleado.comercio = comercio
        try:
            empleado.save()
        except IntegrityError:
            raise DuplicatedPinError()

        serial = EmpleadoSerializer(empleado)

        return Response(serial.data)

    def put(self, request, *args, **kwargs):
        comercio = request.user
        try:
            uuid_empleado = kwargs['uuid_empleado']
        except KeyError:
            raise NoEmpleadoError()

        try:
            nombre = request.data["nombre"]
            apellidos = request.data["apellidos"]
            pin = request.data["pin"]
            activo = request.data["activo"] != "0"
        except KeyError:
            raise IncompleteDataError()

        try:
            empleado = comercio.empleados.get(uuid=uuid_empleado)
        except (Empleado.DoesNotExist, ValidationError):
            raise InvalidEmpleadoError()
        empleado.nombre = nombre
        empleado.apellidos = apellidos
        empleado.pin = pin
        empleado.activo = activo
        try:
            empleado.save()
        except IntegrityError:
            raise DuplicatedPinError()

        serial = EmpleadoSerializer(empleado)

        return Response(serial.data)

    def delete(self, request, *args, **kwargs):
        comercio = request.user
        try:
            uuid_empleado = kwargs['uuid_empleado']
        except KeyError:
            raise NoEmpleadoError()

        try:
            empleado = comercio.empleados.get(uuid=uuid_empleado)
        except (Empleado.DoesNotExist, ValidationError):
            raise InvalidEmpleadoError()
        empleado.delete()

        return Response()

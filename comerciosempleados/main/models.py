import uuid as _uuid

from django.db import models


class Comercio(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=_uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    email_contacto = models.EmailField(max_length=50, null=True, blank=True)
    telefono_contacto = models.CharField(max_length=15, null=True, blank=True)
    api_key = models.UUIDField(default=_uuid.uuid4, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def is_authenticated(self):
        return True


class Empleado(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=_uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    pin = models.CharField(max_length=6)
    comercio = models.ForeignKey('main.Comercio', related_name='empleados',
                                 on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('pin', 'comercio', )

from rest_framework import serializers

from comerciosempleados.main.models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid")
    nombre_completo = serializers.SerializerMethodField()

    def get_nombre_completo(self, obj):
        return obj.nombre + " " + obj.apellidos

    class Meta:
        model = Empleado
        fields = ('id', 'nombre_completo', 'pin', 'fecha_creacion', 'activo')

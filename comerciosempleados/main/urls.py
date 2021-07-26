from django.urls import path, re_path

from comerciosempleados.main import views

app_name = "main"

urlpatterns = [
    re_path(r'^empleados/?$', views.EmpleadosViews.as_view(), name="empleados"),
    re_path(r'^empleados/(?P<uuid_empleado>[0-9A-Za-z_\-]+)/?$', views.EmpleadosViews.as_view(), name="empleado"),
]


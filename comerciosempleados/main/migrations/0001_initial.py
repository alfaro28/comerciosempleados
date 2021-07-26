# Generated by Django 3.2.5 on 2021-07-26 19:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('email_contacto', models.EmailField(blank=True, max_length=50, null=True)),
                ('telefono_contacto', models.CharField(blank=True, max_length=15, null=True)),
                ('api_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('pin', models.CharField(max_length=6)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
                ('comercio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='main.comercio')),
            ],
            options={
                'unique_together': {('pin', 'comercio')},
            },
        ),
    ]

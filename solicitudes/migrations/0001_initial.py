# Generated by Django 4.0.2 on 2022-03-04 15:49

from django.db import migrations, models
import django.db.models.deletion
import django.forms.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('rutNit', models.CharField(max_length=45, primary_key=django.forms.fields.CharField, serialize=False)),
                ('ticket', models.IntegerField()),
                ('nombre', models.CharField(max_length=45)),
                ('razonSocial', models.CharField(max_length=45)),
                ('numProveedor', models.CharField(max_length=45)),
                ('fecha', models.DateField()),
                ('vinculacion', models.CharField(max_length=45)),
                ('marca_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitudes.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('solicitudes_rutNit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitudes.solicitudes')),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_rename_marca_id_solicitudes_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
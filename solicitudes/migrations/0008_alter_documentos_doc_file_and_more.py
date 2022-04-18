# Generated by Django 4.0.2 on 2022-04-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0007_alter_documentos_doc_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='doc_file',
            field=models.FileField(default='', upload_to='proveedores/'),
        ),
        migrations.AlterField(
            model_name='solicitudes',
            name='vinculacion',
            field=models.CharField(choices=[('vinculacion', 'Vinculación'), ('actualizacion', 'Actualización')], max_length=45),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0006_alter_documentos_doc_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='doc_file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-09 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_documentos_doc_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitudes',
            old_name='marca_id',
            new_name='marca',
        ),
    ]

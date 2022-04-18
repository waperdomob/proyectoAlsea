# Generated by Django 4.0.2 on 2022-04-10 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0009_alter_encuestas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadAUD',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadCC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Trasferencia...)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadFC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Cuentas por pagar)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadFT',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Tesorería: Pago de cajas menores y...)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadFV',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Ventas POS ...)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadGA',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadHSEQ',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadLEGAL',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadMC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadRHC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Contratación)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadRHN',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Nomina)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadSSCA',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadSSCC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadSSCE',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Entrega de insumos por parte de proveedores ...)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='amabilidadTEC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadAUD',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadCC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadFC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Cuentas por pagar)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadFT',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Tesorería: Pago de cajas menores y...)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadFV',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Ventas POS ...)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadGA',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadHSEQ',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadLEGAL',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadMC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadRHC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Contratación)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadRHN',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Nomina)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadSSCA',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadSSCC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadSSCE',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Entrega de insumos ...)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='efectividadTEC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteAUD',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Mesa de ayuda)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteCC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Trasferencia de ordenes y servicio al usuario final)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteFC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Cuentas por pagar)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteFT',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Tesorería: Pago de cajas menores y recolección de dinero PROSEGUR)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteFV',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Ventas POS y Cuentas por cobrar)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteGA',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Arriendos y vigilancia)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteHSEQ',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteLEGAL',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteMC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Comunicación de campañas...)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteRHC',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Contratación)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteRHN',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Nomina)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteSSCA',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(AXIONLOG)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteSSCC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Compras)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteSSCE',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Entrega de insumos por parte de proveedores; NO AXIONLOG)'),
        ),
        migrations.AlterField(
            model_name='encuestas',
            name='soporteTEC',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='1', help_text='(Sistema de venta POS...'),
        ),
    ]
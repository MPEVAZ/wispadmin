# Generated by Django 4.0.6 on 2022-07-30 23:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, verbose_name='Usuario')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre cliente')),
                ('telephone', models.CharField(max_length=15, verbose_name='Telefono')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre Paquete')),
                ('down', models.CharField(max_length=50, verbose_name='Velocidad Descarga')),
                ('up', models.CharField(max_length=50, verbose_name='Velocidad Subida')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Paquete',
                'verbose_name_plural': 'Paquetes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Zon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre zona')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mes')),
                ('corte', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de corte')),
                ('paid_out', models.BooleanField(null=True, verbose_name='Pagado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='client',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pack', verbose_name='Paquete'),
        ),
        migrations.AddField(
            model_name='client',
            name='zon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.zon', verbose_name='Zona'),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-03 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0011_auto_20190603_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='cogio_rastreio',
            new_name='codigo_rastreio',
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-12 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0004_alter_trademodel_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='trademodel',
            table='epex_12_20_12_13',
        ),
    ]
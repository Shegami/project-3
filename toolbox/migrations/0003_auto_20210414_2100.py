# Generated by Django 3.2 on 2021-04-14 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0002_auto_20210414_2059'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='Invoices',
            new_name='Invoice',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
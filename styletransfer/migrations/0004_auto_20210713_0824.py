# Generated by Django 3.1.2 on 2021-07-13 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('styletransfer', '0003_auto_20210713_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='session_id',
            new_name='session',
        ),
        migrations.RenameField(
            model_name='styleimg',
            old_name='model_id',
            new_name='model',
        ),
    ]

# Generated by Django 3.1.2 on 2021-07-15 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('styletransfer', '0004_auto_20210713_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=125, null=True)),
            ],
            options={
                'db_table': 'theme',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='styleimg',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='styletransfer.theme'),
        ),
    ]

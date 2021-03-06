# Generated by Django 2.1.7 on 2019-03-23 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('speeddate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 23, 19, 11, 44, 817833, tzinfo=utc), verbose_name='When changed'),
        ),
        migrations.AlterField(
            model_name='question',
            name='insert_date',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-11 21:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assistance', '0004_auto_20191112_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burial',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 21, 27, 9, 219767, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scholar',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 21, 27, 9, 219767, tzinfo=utc)),
        ),
    ]

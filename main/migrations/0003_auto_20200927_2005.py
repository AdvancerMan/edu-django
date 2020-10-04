# Generated by Django 3.1.1 on 2020-09-27 20:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200927_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 27, 20, 4, 56, 450595, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(default='No name', max_length=16),
            preserve_default=False,
        ),
    ]

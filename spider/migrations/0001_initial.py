# Generated by Django 3.1.1 on 2020-10-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('power', models.FloatField()),
                ('defense', models.FloatField()),
                ('health', models.FloatField()),
                ('is_attacker', models.BooleanField()),
            ],
        ),
    ]

# Generated by Django 3.2.6 on 2022-04-19 18:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220417_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='alt_number',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 18, 12, 57, 788618, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='discountpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 18, 12, 57, 787621, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rewardpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 18, 12, 57, 786623, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.2.6 on 2022-04-17 13:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220417_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 13, 10, 55, 430133, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='discountpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 13, 10, 55, 428130, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rewardpointsystem',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 13, 10, 55, 426137, tzinfo=utc)),
        ),
    ]

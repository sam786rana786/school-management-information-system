# Generated by Django 3.0.3 on 2020-02-18 17:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200217_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 18, 17, 3, 39, 931423, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
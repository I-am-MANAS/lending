# Generated by Django 5.0.3 on 2024-03-20 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('byaaj', '0003_remove_customer_amound_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='amound_paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

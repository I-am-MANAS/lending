# Generated by Django 5.0.3 on 2024-03-20 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('byaaj', '0002_remove_customer_profile_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='amound_paid',
        ),
    ]

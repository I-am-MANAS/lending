# Generated by Django 5.0.3 on 2024-03-21 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('byaaj', '0008_customer_password_owner_customer_owner_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='Owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='byaaj.owner'),
        ),
    ]
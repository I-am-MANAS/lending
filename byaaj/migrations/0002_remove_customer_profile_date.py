# Generated by Django 5.0.3 on 2024-03-20 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('byaaj', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_date',
        ),
    ]

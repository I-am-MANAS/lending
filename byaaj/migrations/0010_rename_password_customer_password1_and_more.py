# Generated by Django 5.0.3 on 2024-03-21 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('byaaj', '0009_remove_owner_customer_customer_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='password',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='customer',
            name='password2',
            field=models.CharField(default='password', max_length=100),
        ),
    ]

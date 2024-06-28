# Generated by Django 5.0.3 on 2024-06-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('byaaj', '0020_customer_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='duration',
        ),
        migrations.AddField(
            model_name='customer',
            name='loan_for_months',
            field=models.PositiveIntegerField(default=0, verbose_name='Months'),
        ),
    ]

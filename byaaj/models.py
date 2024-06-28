from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator

# Create your models here.


# class Status(AbstractUser):
#     is_admin = models.BooleanField('Is_admin', default=False)
#     is_customer = models.BooleanField('Is_customer', default=True)
#     # groups = models.ManyToManyField(Group, related_name='status_set')
#     # user_permissions = models.ManyToManyField(
#     #     Permission, related_name='status_set')


class User1(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)


class Owner(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    name = models.CharField(max_length=100, default='name')
    password = models.CharField(max_length=100, default='password')
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.name


class Customer(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    # DURATION_CHOICES = (
    #     ('months', 'Months'),
    #     ('weeks', 'Weeks'),
    #     ('days', 'Days')
    # )
    name = models.CharField(max_length=200, default='name')
    password = models.CharField(max_length=100, default='password')
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    security = models.ImageField(blank=True, null=True)
    passbook = models.ImageField(blank=True, null=True)
    Aadhar = models.ImageField(blank=True, null=True)
    date_issued = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)  # have to add parameter as
    # is_given = True because when money given will be set whem instance created
    # and auto_now will update everytime when saved
    payment_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    loan_for_months = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)] ,verbose_name='Months')
    # duration = models.CharField(
    #     max_length=100, null=True, choices=DURATION_CHOICES, blank=True
    # )
    amount_issued = models.FloatField(blank=True, null=True)
    amound_paid = models.FloatField(default=0)
    logs = models.TextField(blank=True, null=True)
    Owner = models.ForeignKey(
        Owner, null=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.name
    
    # def convert_days_to_months(self):
    #     # Get the current year
    #     current_year = datetime.now().year
        
    #     # Check if the current year is a leap year
    #     is_leap_year = calendar.isleap(current_year)

    #     # Define days in each month based on leap year or non-leap year
    #     if is_leap_year:
    #         days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #     else:
    #         days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Convert excess days into months
        # for days in days_in_month:
        #     if self.days >= days:
        #         self.months += 1
        #         self.days -= days
        #     else:
        #         break

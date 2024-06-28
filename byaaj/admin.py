from django.contrib import admin
from .models import User1, Customer, Owner

# Register your models here.


@admin.register(User1)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_created',
                    'date_issued', 'payment_date', 'status']
    list_display_links = ['id', 'name', 'date_created',
                          'date_issued', 'payment_date', 'status']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_created', 'status']
    list_display_links = ['id', 'name', 'date_created', 'status']


# @admin.register(Status)
# class StatusAadmin(admin.ModelAdmin):
#     list_display = ['username', 'is_customer', 'is_admin', 'password']

from django.db.models import Q, Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from byaaj.models import Customer, Owner
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.template import RequestContext
# from django.shortcuts import render_to_response
from datetime import datetime, timedelta

# Create your views here.


@unauthenticated_user
def registerpage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('username')
            Password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = form.save()
            customer_group = Group.objects.get(name='customer')
            user.groups.add(customer_group)
            Customer.objects.create(
                name=Username, email=email, password=Password, status='Active')
            messages.success(
                request, 'Account was created for ' + Username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'byaaj/register.html', context)
    # return render("byaaj/register.html", context, context_instance=RequestContext(request))


@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is Incorrect')
    context = {}
    return render(request, 'byaaj/login.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['owner'])
@admin_only
def home(request):
    x = datetime.now()
    queryset = Customer.objects.all()
    total_customers_active = queryset.filter(status='Active').count()
    total_customers_inactive = (queryset.count())-(total_customers_active)
    total_amount_given_to_active_users = queryset.filter(status='Active').aggregate(total_amount=Sum('amount_issued'))['total_amount'] or 0
    total_customers = {'total_customers_active':total_customers_active, 'total_customers_inactive':total_customers_inactive, 'total_amount_issued_to_active_customer': total_amount_given_to_active_users}
    return render(request, 'byaaj/dashboard.html', {'date': x,  'total_customers': total_customers})


def logoutt(request):
    logout(request)
    return redirect('login')


def random(request):
    return render(request, 'byaaj/random.html')


def userpage(request):
    context = {}
    return render(request, 'byaaj/user.html', context)


@admin_only
def customer(request):  
    customers = Customer.objects.all()
    final_payment_dates = []
    missing_fields_list = []
    for customer in customers:
        missing_fields = []
        if not customer.security:
            missing_fields.append("Security")
        if not customer.Aadhar:
            missing_fields.append("Aadhar")
        if not customer.passbook:
            missing_fields.append("Passbook")
        missing_fields_list.append(missing_fields)
        final_payment_date = add_months_and_adjust(customer.date_issued, customer.loan_for_months)
        final_payment_dates.append(final_payment_date)
    customers_and_missing_fields = zip(customers, missing_fields_list, final_payment_dates)
    return render(request, 'byaaj/customer.html', {'customers_and_missing_fields': customers_and_missing_fields})


def interest(request):
    return render(request, 'byaaj/interest.html')

def add_months_and_adjust(issue_date, months):
    """Add the given number of months to the issue date and adjust if necessary."""
    year = issue_date.year
    day = issue_date.day
    if day > 28:
        day = 1
        if months==1:
            months = 2
    month = issue_date.month + months

    # Handle the case where the month exceeds 12
    while month > 12:
        year += 1
        month -= 12
    final_date = datetime(year, month, day)
    return final_date

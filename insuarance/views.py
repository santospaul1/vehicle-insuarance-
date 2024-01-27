from datetime import timezone
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

import insuarance
from insuarance.forms import CustomerForm, PolicyForm, VehicleForm
from insuarance.models import Customer, Policy, Vehicle

from django.contrib import messages
from django.shortcuts import render, redirect
from insuarance.forms import CustomerForm

def dashboard(request):
    count_customer = Customer.objects.count()
    count_policies = Policy.objects.count()
    count_vehicle = Vehicle.objects.count()
    context = {
        'count_vehicle':count_vehicle,
        'count_policies':count_policies,
        'count_customer':count_customer,

    }
    return render(request, 'dashboard.html', context)

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Saving the form after accessing cleaned_data
            customer = form.save()
            messages.success(request, 'New Customer has been added successfully')
            return redirect('insuarance:view_customers')  # Redirect to the view_customers page
    else:
        form = CustomerForm()

    return render(request, 'add_customer.html', {'form': form})

def view_customers(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})
def view_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'view_customer.html', {'customer': customer})
def add_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            policy = form.save()
            messages.success(request,"New policy has been added")
            return redirect('insuarance:view_policy')
    else:
        form = PolicyForm()
    return render(request, 'add_policy.html', {'form': form})
def view_policy(request):
    policies = Policy.objects.all()
    for policy in policies:
        if policy.end_date < timezone.now().date():
            if policy.status =='Active':
                policy.status = 'Expired'
                policy.save()
            # If the end date is past today's date, update the policy status to 'Expired'

    return render(request, 'view_policy.html', {'policies': policies})
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save()
            messages.success(request, "Vehicle added successfully")
            return redirect('insuarance:view_vehicles')
    else:
        form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form': form})
def view_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'view_vehicles.html', {'vehicles':vehicles})

def view_vehicle(request,number_plate):
    vehicle = get_object_or_404(Vehicle, id=number_plate)

    return render(request, 'view_vehicle.html', {'vehicle': vehicle})
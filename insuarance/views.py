from datetime import timezone
from PIL import Image, ImageEnhance
import pytesseract
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from insuarance.forms import CustomerForm, PolicyForm, VehicleForm, ImageUploadForm
from insuarance.models import Customer, Policy, Vehicle
from django.contrib import messages



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
    search_term = request.GET.get('search', '')  # Get search query from GET request
    if search_term:
        customers = Customer.objects.filter(
            Q(first_name__icontains=search_term) |  # Search in name field
            Q(email__icontains=search_term) |  # Search in email field
            Q(last_name__icontains=search_term)
            # Add more fields to search as needed
        )
    else:
        customers = Customer.objects.all()  # Fetch all customers if no search term
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
def update_policy(request):
    policies = Policy.objects.all()
    for policy in policies:
        date_difference = policy.end_date - policy.start_date
        policy.date_difference = date_difference.days
        if policy.status == 'Expired' or 'Canceled':
            amount = policy.date_difference * 100
            policy.premium_amount = amount
            policy.status = 'Active'
            policy.save()
    return render(request, 'update_policy.html', {'policies': policies})

#ocr app
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((800, 600))  # Resize to an optimal size
    img = img.convert('L')  # Convert to grayscale
    img = img.point(lambda p: p > 150 and 255)  # Apply adaptive thresholding
    return img
def perform_ocr(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)

    # Enhance image if needed (adjust the factor as required)
    enhancer = ImageEnhance.Contrast(preprocessed_image)
    preprocessed_image = enhancer.enhance(2.0)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(preprocessed_image, config='--psm 6')

    return text

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image to a temporary location
            uploaded_image = form.cleaned_data['image']
            temp_image_path = '/home/santos/Pictures/Screenshots/one.png'
            with open(temp_image_path, 'wb') as temp_image:
                temp_image.write(uploaded_image.read())

            # Perform OCR on the image
            extracted_text = perform_ocr(temp_image_path)

            # Render the result in the template
            return render(request, 'ocr_result.html', {'extracted_text': extracted_text})
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})
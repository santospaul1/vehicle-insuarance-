from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Expired', 'Expired'),
    ('Canceled', 'Canceled'),
)


class Policy(models.Model):
    policy_number = models.CharField(max_length = 50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    premium_amount = models.IntegerField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Active'
    )
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='policies', default=None)

    def __str__(self):
        return f"{self.policy_number}"
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dls_no = models.CharField(null=True,max_length=30, unique=True)
    id_number = models.IntegerField(unique=True)
    email = models.EmailField(null=True, unique=True)
    phone_no = models.CharField(default=0,max_length=15)
    address = models.CharField(max_length=30, default='unknown')
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Male'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vehicle(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    number_plate = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=30)
    year = models.DateField()
    milleage = models.IntegerField(default=0)
    vehicle_price = models.FloatField(default=0)
    def __str__(self):
        return f"{self.number_plate} "







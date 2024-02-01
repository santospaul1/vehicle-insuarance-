from django import forms
from django.forms import DateInput

from insuarance.models import Customer, Policy, Vehicle


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'gender',
            'id_number',
            'email',
            'phone_no',
            'dls_no',
            'address',

        ]

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = [
            'policy_number',
            'start_date',
            'end_date',
            'vehicle',
            'premium_amount',
            'status',
        ]
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        policy = super().save(commit=False)

        # Calculate premium_amount based on date difference
        date_difference = policy.end_date - policy.start_date
        premium_amount = date_difference.days * 100

        # Set the calculated premium_amount
        policy.premium_amount = premium_amount

        if commit:
            policy.save()

        return policy


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'owner',
            'make',
            'model',
            'type',
            'number_plate',
            'color',
            'year',
            'milleage',
            'vehicle_price',
        ]
        widgets = {
            'year': DateInput(attrs={'type': 'date'})
        }

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
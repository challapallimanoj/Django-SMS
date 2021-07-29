from django import forms
from django.forms import ModelForm, fields, widgets
from .models import *
class BookingForm(forms.ModelForm):
    class Meta:
        model=Bookings
        fields = ['name','number','email','service','date','address','state','city','pincode']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter Full Name'}),
            'number':forms.NumberInput(attrs={'placeholder':'Mobile Number'}),
            'address':forms.TextInput(attrs={'placeholder':'Enter Address'}),
            'city':forms.TextInput(attrs={'placeholder':'Enter City Name'}),
            'pincode':forms.NumberInput(attrs={'placeholder':'Pin/Zip Code'}),
        }

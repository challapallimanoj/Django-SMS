from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Services Model


class Enquiry(models.Model):
    branch = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    supervisor = models.CharField(max_length=200)


class Services(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    link = models.CharField(max_length=500, default='url')
    minimum_charges = models.FloatField(default=0.00)
    employee_count = models.IntegerField(default=1)


# Bookings model
state_choice = (
    ("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "),
    ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh",
                                             "Chhattisgarh"), ("Goa", "Goa"),
    ("Gujarat", "Gujarat"), ("Haryana",
                             "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand",
                                                   "Jharkhand"), ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"), ("Madhya Pradesh",
                           "Madhya Pradesh"), ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram",
                                                         "Mizoram"), ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"), ("Punjab", "Punjab"), ("Rajasthan",
                                                 "Rajasthan"), ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"), ("Telangana",
                                   "Telangana"), ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand",
                                         "Uttarakhand"), ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Islands",
     "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"),
    ("Dadra and Nagar Haveli",
     "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"),
    ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi",
                                     "National Capital Territory of Delhi"),
    ("Puducherry", "Puducherry")
)

service_choice = (
    ('PAINTING', 'PAINTING'), ('CARPENTERING', 'CARPENTERING'),
    ('HOUSE SHIFTING', 'HOUSE SHIFTING'), ('FOOD CATERING', 'FOOD CATERING'), ('LAUNDRY/DRY WASH', 'LAUNDRY/DRY WASH'), ('PLUMBERING', 'PLUMBERING'), ('CONSTRUCTION',
                                                                                                                                                       'CONSTRUCTION'), ('MECHANICS', 'MECHANICS'), ('INTERIOR DESIGNING', 'INTERIOR DESIGNING'), ('TECHNICIANS', 'TECHNICIANS'), ('PRINTING', 'PRINTING'), ('UNISEX PARLOR', 'UNISEX PARLOR'), ('OTHER', 'OTHER')
)


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    number = models.BigIntegerField()
    email = models.EmailField()
    service = models.CharField(max_length=150, choices=service_choice)
    date = models.DateField()
    address = models.TextField()
    state = models.CharField(max_length=150, choices=state_choice)
    city = models.CharField(max_length=150)
    pincode = models.IntegerField()

# Questions for faq model


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()

# Painting catgories


class Painting(models.Model):
    category = models.CharField(max_length=200)
    type = models.CharField(max_length=150)
    suits = models.CharField(max_length=500)
    brand = models.CharField(max_length=200)
    price = models.FloatField()
    rating = models.FloatField()
    img = models.ImageField(upload_to='paint', default='DEFAULT VALUE')


class HouseShifting(models.Model):
    category = models.CharField(max_length=250)
    type = models.CharField(max_length=200)
    price = models.FloatField()
    max_limit = models.IntegerField()
    rating = models.FloatField()
    img = models.ImageField(upload_to='houseshift')


class Carpentering(models.Model):
    img = models.ImageField(upload_to='carpenter', default='DEFAULT VALUE')
    category = models.CharField(max_length=250)
    type = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    lock = models.CharField(max_length=250)
    hinges = models.CharField(max_length=200)
    price = models.FloatField()
    rating = models.FloatField()

# imports
from django.db.models import query
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.safestring import mark_safe
from .models import *
from django.contrib.auth.models import User
import wolframalpha
import wikipedia
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import pandas as pd
from .forms import*

# Create your views here.

# Enquiry view


def enquiry(request):
    item = Enquiry.objects.all()
    return render(request, 'enquiry.html', {'item': item})


# Page not found view


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)

# Payment Page


@login_required
def payment(request):
    return render(request, 'payment.html')

# Profile and bookings page


@login_required
def profile(request):
    u = request.user
    items = Bookings.objects.filter(user=u.id)
    return render(request, 'profile.html', {'items': items})

# Edit or update page


@login_required
def editpage(request, list_id):
    item = Bookings.objects.get(pk=list_id)
    mydictonary = {
        "id": item.id,
        "name": item.name,
        "number": item.number,
        "service": item.service,
        "date": item.date
    }
    return render(request, 'editbooking.html', context=mydictonary)

# Edit fuction


@login_required
def edit(request, list_id):
    if request.method == 'POST':
        item = Bookings.objects.get(pk=list_id)
        item.name = request.POST['name']
        item.number = request.POST['number']
        item.service = request.POST['service']
        item.date = request.POST['date']
        import datetime
        updated_at = datetime.datetime.now()
        item.created_at = updated_at
        mydict = {'name': item.name, 'number': item.number,
                  'service': item.service, 'date': item.date}
        item.save()
        html_template = 'update_email.html'
        html_message = render_to_string(html_template, context=mydict)
        subject = 'Update or Resheduled'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [item.email]
        message = EmailMessage(subject, html_message,
                               email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
        return redirect("profile")
    else:
        return render(request, 'editbooking.html')

# cancel booking


@login_required
def delete(request, list_id):
    item = Bookings.objects.get(pk=list_id)
    mydict = {'name': item.name}
    item.delete()
    html_template = 'cancelbooking_email.html'
    html_message = render_to_string(html_template, context=mydict)
    subject = 'Cancel Booking'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [item.email]
    message = EmailMessage(subject, html_message,
                           email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()
    return redirect("profile")

# Home page


def main(request):
    return render(request, 'main.html')

# Services Page


@login_required
def services(request):
    sers = Services.objects.all()
    return render(request, 'services.html', {'sers': sers})

# Bookings form


@login_required
def details(request):
    form=BookingForm
    return render(request, 'booking.html',{'form':form})

# Bookings function


@login_required
def booking(request):
    if request.method == "POST":
        u = request.user
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        service = request.POST['service']
        date = request.POST['date']
        address = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        book = Bookings(user=u, name=name, number=number, email=email, service=service, date=date,
                        address=address, state=state, city=city, pincode=pincode)
        mydict = {'name': name, 'number': number, 'email': email, 'service': service,
                  'date': date, 'address': address, 'state': state, 'city': city, 'pincode': pincode}
        # selected service counting
        selected_service = service
        selected_date = date
        counting = Bookings.objects.filter(date=selected_date).values()
        df = pd.DataFrame(counting)
        if(df.empty):
            book.save()
            messages.info(
                request, mark_safe('Successfully booked a Service Check Your <a href="profile" style="color:blue;">Bookings</a>'))
            html_template = 'bookingconfromation_mail.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Just One Step Away In Bookings'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            return redirect("services")
        else:
            count = len(df[df['service'] == selected_service])
            print(count)
            counting1 = Services.objects.all().values()
            df1 = pd.DataFrame(counting1)
            count1 = df1.loc[df1.name == selected_service,
                             'employee_count'].to_string(index=False)
            count2 = int(count1)
            print(selected_service)
            print(selected_date)
            print(count)
            print(count2)
            # checking availbality (incase of available)
            if count > count2:
                messages.info(
                request, 'Sorry To Say Workers were Busy for Selected Service & Date ! You can Book on Another Date')
                return redirect("services")
    else:
        return redirect("details")


# bot page
@login_required
def botpage(request):
    return render(request, 'bot.html')


# bot function

@login_required
def bot_search(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("7366WT-YAKR9J9EW8")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'bot.html', {'ans': ans, 'query': query})

    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'bot.html', {'ans': ans, 'query': query})

        except Exception:
            try:
                ans = get_site_query(query)
                return render(request, 'bot.html', {'ans': ans, 'query': query})

            except Exception:
                ans = 'FOUND NOTHING'
                return render(request, 'bot.html', {'ans': ans, 'query': query})


@login_required
def get_site_query(request, query):
    help = ['help', 'help me!']
    signin = ['I cant login into my account',
              'signinin failed', 'signin issue']
    signup = ['I cant signup', 'signup failed', 'signup issue']
    if query == help:
        ans = "To get instant help call to 8247729832 (or) Mail to serviceverse@gmail.com"

    elif query == signin:
        ans = "Enter valid credentails or incase of forgot password reset it through clicking the forgot passowrd option in signin page"
    elif query == signup:
        ans = "Incase of unable to create an account signup with the google option available in the signup page"
    return ans


# faq Page

@login_required
def faqpage(request):
    faqs = Question.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})

# Services Catagories


@login_required
def paintingcatagories(request):
    item = Painting.objects.all()
    return render(request, 'paint-service.html', {'item': item})


@login_required
def carpentercatagories(request):
    item = Carpentering.objects.all()
    return render(request, 'carpenter-service.html', {'item': item})


@login_required
def houseshiftingcatagories(request):
    item = HouseShifting.objects.all()
    return render(request, 'houseshifting-service.html', {'item': item})


def foodcateringcatagories(request):
    return render(request, 'catering-service.html')


def laundarycatagories(request):
    return render(request, 'laundary-service.html')


def plumbercatagories(request):
    return render(request, 'plumber-service.html')


def constructioncatagories(request):
    return render(request, 'construction-service.html')


def mechanicscatagories(request):
    return render(request, 'mechanic-service.html')


def interiordesigningcatagories(request):
    return render(request, 'interiordesign-service.html')


def technicianscatagories(request):
    return render(request, 'technician-service.html')


def printingcatagories(request):
    return render(request, 'printing-service.html')


def parlourcatagories(request):
    return render(request, 'parlour-service.html')

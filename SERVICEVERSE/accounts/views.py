from typing import Counter
from main.models import Bookings, Services
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.db.models import Avg, Count, Min, Sum
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import permission_required, user_passes_test
import pandas as pd
import math
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Oh No,Invalid Username or Password !')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Huff ,Username already exist')
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Come On, Email was already Taken !')
            return redirect("register")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            mydict = {'username': username}
            user.save()
            html_template = 'register_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome to Service-Verse'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            return redirect("login")
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


@permission_required('auth.view_user')
def graphs_rate(request):
    counter = User.objects.count()
    average = User.objects.filter(
        is_superuser=True).aggregate(Count('is_superuser'))
    services = Services.objects.count()
    bookings = Bookings.objects.all().count()
    active = get_all_logged_in_users()
    inactive = get_inactive_users()
    df = get_state_data()
    df1 = get_services_data()
    df2 = get_profit_data()
    average_profit = get_average_profit()
    lb = get_lowerboundary()
    emp = get_employee()
    mydict = {
        'counter': counter,
        'average': average,
        'services': services,
        'bookings': bookings,
        'active': active,
        'inactive': inactive,
        'df': df,
        "df1": df1,
        'df2': df2,
        'average_profit': average_profit,
        'lb': lb,
        'emp': emp
    }
    print(df)
    return render(request, "graphs.html", context=mydict)


def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    list = User.objects.filter(id__in=uid_list)
    return list.count()


def get_inactive_users():
    count = User.objects.count()
    result = count-get_all_logged_in_users()
    return result

# services in states visuzalization


def get_state_data():
    df = Bookings.objects.all().values()
    df = pd.DataFrame(df)
    x1 = len(df[df['state'] == 'Andhra Pradesh'])
    x2 = len(df[df['state'] == 'Uttar Pradesh'])
    x3 = len(df[df['state'] == 'Haryana'])
    x4 = len(df[df['state'] == 'Arunachal Pradesh'])
    x5 = len(df[df['state'] == 'Assam'])
    x6 = len(df[df['state'] == 'Bihar'])
    x7 = len(df[df['state'] == 'Chhattisgarh'])
    x8 = len(df[df['state'] == 'Goa'])
    x9 = len(df[df['state'] == 'Gujarat'])
    x10 = len(df[df['state'] == 'Jammu and Kashmir '])
    x11 = len(df[df['state'] == 'Jharkhand'])
    x12 = len(df[df['state'] == 'West Bengal'])
    x13 = len(df[df['state'] == 'Karnataka'])
    x14 = len(df[df['state'] == 'Kerala'])
    x15 = len(df[df['state'] == 'Madhya Pradesh'])
    x16 = len(df[df['state'] == 'Maharashtra'])
    x17 = len(df[df['state'] == 'Manipur'])
    x18 = len(df[df['state'] == 'Meghalaya'])
    x19 = len(df[df['state'] == 'Mizoram'])
    x20 = len(df[df['state'] == 'Nagaland'])
    x21 = len(df[df['state'] == 'Orissa'])
    x22 = len(df[df['state'] == 'Himachal Pradesh'])
    x23 = len(df[df['state'] == 'Punjab'])
    x24 = len(df[df['state'] == 'Rajasthan'])
    x25 = len(df[df['state'] == 'Telangana'])
    x26 = len(df[df['state'] == 'Chandigarh'])
    x27 = len(df[df['state'] == 'Andaman and Nicobar Islands'])
    x28 = len(df[df['state'] == 'Dadra and Nagar Haveli'])
    x29 = len(df[df['state'] == 'Daman and Diu'])
    x30 = len(df[df['state'] == 'National Capital Territory of Delhi'])
    x31 = len(df[df['state'] == 'Lakshadweep'])
    x32 = len(df[df['state'] == 'Puducherry'])
    count = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16,
             x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32]
    print(count)
    return count

# services visualizations


def get_services_data():
    df = Bookings.objects.all().values()
    df = pd.DataFrame(df)
    x1 = len(df[df['service'] == 'PAINTING'])
    x2 = len(df[df['service'] == 'CARPENTERING'])
    x3 = len(df[df['service'] == 'HOUSE SHIFTING'])
    x4 = len(df[df['service'] == 'FOOD CATERING'])
    x5 = len(df[df['service'] == 'LAUNDRY/DRY WASH'])
    x6 = len(df[df['service'] == 'PLUMBERING'])
    x7 = len(df[df['service'] == 'CONSTRUCTION'])
    x8 = len(df[df['service'] == 'MECHANICS'])
    x9 = len(df[df['service'] == 'INTERIOR DESIGNING'])
    x10 = len(df[df['service'] == 'TECHNICIANS'])
    x11 = len(df[df['service'] == 'PRINTING'])
    x12 = len(df[df['service'] == 'UNISEX PARLOR'])
    x13 = len(df[df['service'] == 'OTHER'])
    count = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]
    return count

# services profit visualization


def get_profit_data():
    df = Services.objects.all().values()
    df = pd.DataFrame(df)
    count = df['minimum_charges'].tolist()
    return count


def get_average_profit():
    df = Services.objects.all().values().aggregate(Avg('minimum_charges'))
    return df


def get_lowerboundary():
    df = Services.objects.all().values()
    df = pd.DataFrame(df)
    count = df['minimum_charges'].tolist()
    print(count)
    sum1 = sum(count)
    res = sum1/300
    res = math.ceil(res)
    return res


def get_employee():
    df = Services.objects.all().values()
    df = pd.DataFrame(df)
    count = df['employee_count'].tolist()
    return count

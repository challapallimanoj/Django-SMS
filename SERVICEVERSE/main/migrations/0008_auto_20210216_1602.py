# Generated by Django 3.1.4 on 2021-02-16 10:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20210216_1555'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Bookings',
        ),
    ]
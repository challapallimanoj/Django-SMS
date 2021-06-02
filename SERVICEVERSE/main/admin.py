from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Question)
admin.site.register(Services)
admin.site.register(Bookings)
admin.site.register(Enquiry)
# Categories of services
admin.site.register(Painting)
admin.site.register(HouseShifting)
admin.site.register(Carpentering)
# Admin Page Decors
admin.site.site_header = 'SERVICE-VERSE'
admin.site.index_title = 'ADMIN'
admin.site.site_title = 'SERVICE-VERSE'

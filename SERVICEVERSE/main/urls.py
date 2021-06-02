from django.conf.urls import include
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # homepage
    path('', views.main, name='main'),
    # services page
    path('services', views.services, name='services'),
    # profile and user bookings page
    path('profile', views.profile, name='profile'),
    # editform page
    path('editpage/<list_id>', views.editpage, name="editpage"),
    # bookings form submit
    path('booking/', views.booking, name='booking'),
    # update submit method
    path('edit/<list_id>', views.edit, name='edit'),
    # booking form page
    path('details', views.details, name='details'),
    # delete or cancel booking
    path("delete/<list_id>", views.delete, name="delete"),
    # bot functionality method
    path('bot_search/', views.bot_search, name='bot_search'),
    # bot page
    path('botpage', views.botpage, name="botpage"),
    # faq page
    path('faqpage', views.faqpage, name="faqpage"),
    # payments page
    path('payment', views.payment, name='payment'),
    # enquiry page
    path('enquiry', views.enquiry, name="enquiry"),
    #catagories in services
    path('paintingcatagories', views.paintingcatagories, name='paintingcatagories'),
    path('carpentercatagories', views.carpentercatagories,
         name='carpentercatagories'),
    path('houseshiftingcatagories', views.houseshiftingcatagories,
         name='houseshiftingcatagories'),
    path('foodcateringcatagories', views.foodcateringcatagories,
         name='foodcateringcatagories'),
    path('laundarycatagories', views.laundarycatagories, name='laundarycatagories'),
    path('plumbercatagories', views.plumbercatagories, name='plumbercatagories'),
    path('constructioncatagories', views.constructioncatagories,
         name='constructioncatagories'),
    path('mechanicscatagories', views.mechanicscatagories,
         name='mechanicscatagories'),
    path('interiordesigningcatagories', views.interiordesigningcatagories,
         name='interiordesigningcatagories'),
    path('technicianscatagories', views.technicianscatagories,
         name='technicianscatagories'),
    path('printingcatagories', views.printingcatagories, name='printingcatagories'),
    path('parlourcatagories', views.parlourcatagories, name='parlourcatagories'),

    # visualization
    #path('graphs_rate', views.graphs_rate, name='graphs_rate')

]
# page not found 404
handler404 = 'main.views.error_404'

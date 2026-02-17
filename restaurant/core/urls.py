from django.urls import path 
from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about"),
    path('services/',services,name="services"),
    path('contact/',contact,name="contact"),
    path('menu/',menu,name="menu"),
    path('testemonial/',testemonial,name="testemonial"),
    path('terms/',terms,name="terms"),
    path('privacy/',privacy,name="privacy"),
    path('register/',register,name="register"),
    path('login/',log_in,name="log_in"),
    path('logout/',log_out,name="log_out"),
    path('pass_change/',pass_change,name="pass_change"),
    
]

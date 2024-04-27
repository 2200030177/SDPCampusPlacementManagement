from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name="home"),
    path('register', register, name="register"),
    path('aboutus', aboutus, name="aboutus"),
    path('services', service, name="services"),
    path('contact', contact, name="contact"),
    path('signupsignin', signupsignin, name="signupsignin"),
    path('cosignupsignin', cosignupsignin, name="cosignupsignin"),
    path('student_verification/', student_verification, name='student_verification'),
    path('company_verification/', company_verification, name='company_verification'),
]

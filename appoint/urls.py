from django.urls import path
from .views import home,book_appointment,contact

urlpatterns = [
    path('',home,name="home"),
    path('book/',book_appointment, name='book_appointment'),
    path('contact/', contact, name='contact'),
]

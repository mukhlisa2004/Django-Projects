from django.urls import path
from .views import hello,about,Home_Viev


urlpatterns=[
    path('', hello, name='hello'),
    path('about/', about, name='about'),
    path('home/', Home_Viev.as_view(), name='home'),

]
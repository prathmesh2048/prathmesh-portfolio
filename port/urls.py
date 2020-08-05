from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('new_request', views.new_request, name='new_request')

]
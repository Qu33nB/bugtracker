from django.urls import path
from bugtracker_app import views

urlpatterns = [ 
    path('', views.index, name='home'),
]

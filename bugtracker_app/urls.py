from django.urls import path
from bugtracker_app import views

urlpatterns = [ 
    path('', views.index, name='home'),
    path('login/', views.loginview),
    path('adduser/', views.adduser),
    path('logout/', views.logoutview)
]

from django.urls import path
from bugtracker_app import views

urlpatterns = [ 
    path('', views.index, name='home'),
    path('login/', views.loginview),
    path('adduser/', views.adduser),
    path('addbug/', views.addbug),
    path('logout/', views.logoutview),
    path('user/<int:id>/', views.user_info, name='user'),
    path('bug/<int:id>/', views.bugs, name='bug'),
    path('editbug/<int:id>/', views.bug_edit, name='editbug'),
    path('inprogress/<int:id>/', views.in_progress_bug, name='inprogress'),
    path('completed/<int:id>/', views.completed_bug, name='completed'),
    path('invalid/<int:id>/', views.invalid_bug, name='invalid'),
]

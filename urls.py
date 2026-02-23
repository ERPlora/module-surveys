from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('surveys/', views.surveys, name='surveys'),
    path('responses/', views.responses, name='responses'),
    path('settings/', views.settings, name='settings'),
]

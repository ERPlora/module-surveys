from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Survey
    path('surveys/', views.surveys_list, name='surveys_list'),
    path('surveys/add/', views.survey_add, name='survey_add'),
    path('surveys/<uuid:pk>/edit/', views.survey_edit, name='survey_edit'),
    path('surveys/<uuid:pk>/delete/', views.survey_delete, name='survey_delete'),
    path('surveys/<uuid:pk>/toggle/', views.survey_toggle_status, name='survey_toggle_status'),
    path('surveys/bulk/', views.surveys_bulk_action, name='surveys_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]

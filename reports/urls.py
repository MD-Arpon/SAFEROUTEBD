from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('report/incident/', views.report_incident, name='report_incident'),
    path('report/streetlight/', views.report_light, name='report_light'),
    path('report/crowd/', views.report_crowd, name='report_crowd'),
    path('list/', views.incident_list, name='incident_list'),
]
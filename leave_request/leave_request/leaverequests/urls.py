
from django.urls import path

from . import views

app_name = "leaverequests"

urlpatterns = [
    path('', views.index, name='index'),
    path('create-profile', views.create_profile, name='create-profile'),
    path('create-request', views.create_request, name='create-request'),
    path('history-log', views.history_log, name='history-log'),
    path('history-admin-log', views.history_admin_log, name='history-admin-log'),
    path('<int:id>/approve-request', views.approve_request, name='approve-request'),
    path('<int:id>/reject-request', views.reject_request, name='reject-request'),
]

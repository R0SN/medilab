from django.urls import path
from . import views
from .views import admin_dashboard


urlpatterns = [
    path('', views.home, name='home'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
]

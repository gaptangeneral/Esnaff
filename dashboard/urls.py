from django.urls import path
from .views import admin_dashboard
app_name = 'dashboard'
urlpatterns = [
    path('admin/', admin_dashboard, name='admin-dashboard'),
]

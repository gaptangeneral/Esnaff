# dashboard/views.py

from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from employee.models import Employee

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Bu sayfaya erişim izniniz yok.")
    
    # Tüm çalışan verilerini al
    employee_list = Employee.objects.all()
    
    # Şablona çalışan verilerini gönder
    return render(request, 'dashboard/admin_dashboard.html', {'employee_list': employee_list})

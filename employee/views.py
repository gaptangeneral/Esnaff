from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .models import Employee, Attendance, Salary
from django.urls import reverse_lazy
from .forms import AttendanceForm, SalaryForm, EmployeeForm
from django.db.models import Count, Avg, Sum

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'object_list'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm  # Özel form kullanılıyor
    template_name = 'employee/employee_form.html'
    success_url = reverse_lazy('employee:employee-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm  # Özel form kullanılıyor
    template_name = 'employee/employee_form.html'
    success_url = reverse_lazy('employee:employee-list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    success_url = reverse_lazy('employee:employee-list')
    
#puantaj

class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'employee/attendance/attendance_form.html'
    success_url = reverse_lazy('employee:attendance-list')

class AttendanceUpdateView(UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'employee/attendance/attendance_form.html'
    success_url = reverse_lazy('employee:attendance-list')


class AttendanceListView(ListView):
    model = Attendance
    template_name = 'employee/attendance/attendance_list.html'
    context_object_name = 'attendance_list'
    

class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = 'employee/attendance/attendance_confirm_delete.html'
    success_url = reverse_lazy('employee:attendance-list')

# MAAŞ İŞLEMLERİ 

class SalaryListView(ListView):
    model = Salary
    template_name = 'employee/salary/salary_list.html'
    context_object_name = 'salaries'

class SalaryCreateView(CreateView):
    model = Salary
    form_class = SalaryForm  # Özel form kullanılıyor
    template_name = 'employee/salary/salary_form.html'
    success_url = reverse_lazy('employee:salary-list')

class SalaryUpdateView(UpdateView):
    model = Salary
    form_class = SalaryForm  # Özel form kullanılıyor
    template_name = 'employee/salary/salary_form.html'
    success_url = reverse_lazy('employee:salary-list')

class SalaryDeleteView(DeleteView):
    model = Salary
    template_name = 'employee/salary/salary_confirm_delete.html'
    success_url = reverse_lazy('employee:salary-list')

class EmployeeStatisticsView(TemplateView):
    template_name = 'employee/employee_statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Toplam Çalışan Sayısı
        total_employees = Employee.objects.count()
        
        # Departman Bazında Çalışan Sayısı
        department_distribution = Employee.objects.values('department').annotate(count=Count('id')).order_by('-count')
        
        # Ortalama Maaş
        average_salary = Employee.objects.aggregate(avg_salary=Avg('salary_amount'))['avg_salary']
        
        # Toplam Maaş
        total_salary = Employee.objects.aggregate(total_salary=Sum('salary_amount'))['total_salary']
        
        # Devamsızlık Oranı
        total_attendance = Attendance.objects.count()
        total_absent = Attendance.objects.filter(is_absent=True).count()
        absence_rate = (total_absent / total_attendance) * 100 if total_attendance > 0 else 0
        
        # Ortalama Yaş
        average_age = Employee.objects.aggregate(avg_age=Avg('age'))['avg_age']
        
        # Çalışanların Cinsiyet Dağılımı
        gender_distribution = Employee.objects.values('gender').annotate(count=Count('id')).order_by('-count')
        
        # Context'e Eklenen Veriler
        context.update({
            'total_employees': total_employees,
            'department_distribution': department_distribution,
            'average_salary': average_salary,
            'total_salary': total_salary,
            'absence_rate': absence_rate,
            'average_age': average_age,
            'gender_distribution': gender_distribution,
        })
        
        return context
    
# employee/forms.py

from django import forms
from .models import Employee, Attendance, Salary
from common.base_forms import BaseForm, DateInput  # Ortak BaseForm ve DateInput

class EmployeeForm(BaseForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'department', 'position', 'salary_amount',
            'hire_date', 'is_active', 'gender', 
            'tckn', 'sgk_number', 'date_of_birth', 'employee_type'
        ]
        widgets = {
            'hire_date': DateInput(),
            'date_of_birth': DateInput(),
        }

class AttendanceForm(BaseForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status', 'worked_hours', 'notes']
        widgets = {
            'date': DateInput(),
        }

class SalaryForm(BaseForm):
    class Meta:
        model = Salary
        fields = [
            'employee',
            'period_start',
            'period_end',
            'gross_salary',
            'bonuses',
            'allowances',
            'total_deductions'
        ]
        widgets = {
            'period_start': DateInput(),
            'period_end': DateInput(),
        }

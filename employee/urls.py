from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    AttendanceListView, 
    AttendanceCreateView,
    SalaryListView, 
    SalaryCreateView, 
    SalaryUpdateView, 
    SalaryDeleteView,
    EmployeeStatisticsView,
    AttendanceUpdateView,
    AttendanceDeleteView
    
)
app_name = 'employee'
urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee-edit'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('attendance/add/', AttendanceCreateView.as_view(), name='attendance-add'),
    path('attendance/<int:pk>/edit/', AttendanceUpdateView.as_view(), name='attendance-update'),
    path('attendance/<int:pk>/delete/', AttendanceDeleteView.as_view(), name='attendance-delete'),
    path('salaries/', SalaryListView.as_view(), name='salary-list'),
    path('salaries/add/', SalaryCreateView.as_view(), name='salary-add'),
    path('salaries/<int:pk>/edit/', SalaryUpdateView.as_view(), name='salary-edit'),
    path('salaries/<int:pk>/delete/', SalaryDeleteView.as_view(), name='salary-delete'),
    path('statistics/', EmployeeStatisticsView.as_view(), name='employee-statistics'),  # İstatistik URL'i

    
]
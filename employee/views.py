from django.shortcuts import render
from django.views.generic import ListView
from employee.models import Employee


class EmployeeListView(ListView):
    template_name = 'employee.html'
    context_object_name = 'employees'
    model = Employee
    paginate_by = 10

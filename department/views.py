from django.shortcuts import render


def department(request):
    return render(request, 'department.html')

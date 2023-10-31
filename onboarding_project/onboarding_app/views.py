from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import EmployeeForm

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      auth_login(request, user)
      return redirect('employee_list')
    else:
      return render(request, 'login.html', {'error': 'Invalid username or password.'})
  else:
    return render(request, 'login.html')
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    context = {"employees": employees}
    return render(request, "employee_list.html", context)
@login_required
def add_employee(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        start_date = request.POST.get('start_date')
        is_onboarded = False  
        employee = Employee.objects.create(first_name=first_name, last_name=last_name, email=email, department=department, start_date=start_date, is_onboarded=is_onboarded)
        employee.save()
        return redirect('employee_list') 
    else:
        return render(request, 'employee_form.html')

@login_required
def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    context = {"employee": employee}
    return render(request, "employee_detail.html", context)

@login_required
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()

    context = {"form": form}
    return render(request, "employee_create.html", context)
@login_required
def employee_mark_onboarded(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.is_onboarded = True
    employee

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def base(request):
    pass
    

@login_required
def employee_update(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy(":employee_detail", kwargs={"pk": pk}))
    else:
        form = EmployeeForm(instance=employee)

    context = {"form": form}
    return render(request, "employee_update.html", context)

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()

    return redirect(reverse_lazy("employee_list"))
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "signup.html", context)

@login_required
def employee_update(request, pk):
  employee = get_object_or_404(Employee, pk=pk)

  if request.method == 'POST':
    employee.first_name = request.POST.get('first_name')
    employee.last_name = request.POST.get('last_name')
    employee.email = request.POST.get('email')
    employee.department = request.POST.get('department')
    employee.start_date = request.POST.get('start_date')
    employee.is_onboarded = bool(request.POST.get('is_onboarded'))

    employee.save()

    return redirect('employee_list')
  else:
    return render(request, 'employee_update.html', {'employee': employee})

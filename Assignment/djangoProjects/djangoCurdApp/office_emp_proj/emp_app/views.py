from django.shortcuts import render, redirect,HttpResponse
from .models import Employee, Role, Department
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'index.html')


def all_emp(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    print(context)
    return render(request, 'view_emp.html', context)



def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept_id = request.POST.get('dept')
        salary = int(request.POST.get('salary'))
        bouns = int(request.POST.get('bouns'))
        role_id = request.POST.get('role')
        phone = int(request.POST.get('phone'))
        hire_date = request.POST.get('hire_date')

        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            dept_id=dept_id,
            salary=salary,
            bouns=bouns,
            role_id=role_id,
            phone=phone,
            hire_date=hire_date
        )
        employee.save()

        return redirect('success_page')

    departments = Department.objects.all()
    roles = Role.objects.all()

    return render(request, 'add_emp.html', {'departments': departments, 'roles': roles})


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
            pass
        except:
            return HttpResponse("Please enter valid id")
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'remove_emp.html',context)

 # try:
    #     employee = Employee.objects.get(pk=employee_id)
    #     employee.delete()
    #     return redirect('success_page')  # Redirect to a success page
    # except Employee.DoesNotExist:
    #     return render(request, 'error_page.html')

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(role__name=role)

        context = {
            'emps': emps
        }
        return render(request, 'view_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')

    else:
        return HttpResponse("An Exception Occurred")



def success_page(request):
    return render(request, 'success.html')

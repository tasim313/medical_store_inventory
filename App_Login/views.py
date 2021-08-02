'''''
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import CustomUser, PharmacyAdmin, PharmacyManager, Employee
from App_Login.user_authenticate import UserAuthenticate
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, AdminInfoForm, ManagerInfoForm, EmployeeInfoForm


def admin_register(request):
    registered = False
    user_form = UserForm()
    admin_info_form = AdminInfoForm()
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        admin_info_form = AdminInfoForm(data=request.POST)
        if user_form.is_valid() and admin_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            admin_info = admin_info_form.save(commit=False)
            admin_info.admin = user
            admin_info.save()
            registered = True

        else:
            user_form = UserForm()
            admin_info_form = AdminInfoForm()
    diction = {'user_form': user_form, 'admin_info_form': admin_info_form, 'registered': registered}
    return render(request, 'App_Login/admin_registration.html', context=diction)


def manager_register(request):
    registered = False
    user_form = UserForm()
    manager_info_form = ManagerInfoForm()
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        manager_info_form = ManagerInfoForm(data=request.POST)
        if user_form.is_valid() and manager_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            manager_info = manager_info_form.save(commit=False)
            manager_info.admin = user
            manager_info.save()
            registered = True

        else:
            user_form = UserForm()
            manager_info_form = ManagerInfoForm()
    diction = {'user_form': user_form, 'manager_info_form': manager_info_form, 'registered': registered}
    return render(request, 'App_Login/manager_registration.html', context=diction)


def employee_register(request):
    registered = False
    user_form = UserForm()
    employee_info_form = EmployeeInfoForm()
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        employee_info_form = EmployeeInfoForm(data=request.POST)
        if user_form.is_valid() and employee_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            employee_info = employee_info_form.save(commit=False)
            employee_info.admin = user
            employee_info.save()
            registered = True

        else:
            user_form = UserForm()
            employee_info_form = EmployeeInfoForm()
    diction = {'user_form': user_form, 'employee_info_form': employee_info_form, 'registered': registered}
    return render(request, 'App_Login/employee_registration.html', context=diction)


def login_page(request):
    return render(request, 'App_Login/login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponse('<h2> Admin</h2>')
            elif user.user_type == "2":
                return HttpResponse('<h2>Manager</h2>')
            else:
                return HttpResponseRedirect(reverse("employee_home"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")
    else:
        return HttpResponse('ha ha')


def logout_user(request):
    logout(request)
    return HttpResponse("<h1>You are logout </h1>")






'''





'''''



def show_login_page(request):
    return render(request, "App_Login/login_page.html")


def login_page(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = UserAuthenticate.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user!=None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponse('<h2> Admin</h2>')
            elif user.user_type == "2":
                return HttpResponse('<h2>Manager</h2>')
            else:
                return HttpResponseRedirect(reverse("employee_home"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")


def add_admin_sign_up(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    lic_no = request.POST.get('lic_no')
    s_name = request.POST.get('s_name')
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    address = request.POST.get('address')

    try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=1)
        user.PharmacyAdmin.lic_no = lic_no
        user.PharmacyAdmin.s_name = s_name
        user.PharmacyAdmin.name = name
        user.PharmacyAdmin.contact = contact
        user.PharmacyAdmin.address = address
        user.save()
        messages.success(request, "Successfully Created Admin")
        return HttpResponseRedirect(reverse("App_Login:login_view"))
    except:
        messages.error(request, "Failed to Create Admin")
        return HttpResponseRedirect(reverse("App_Login:login_view"))


def show_admin_sign_up(request):
    return render(request, 'App_Login/sign_up.html')


def add_manager_sign_up(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    pharmacy_id = request.POST.get('pharmacy_id ')
    try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=2)
        user.PharmacyManager.name = name
        user.PharmacyManager.contact = contact
        user.PharmacyManager.address = address
        pharmacy_obj = PharmacyAdmin.objects.get(id=pharmacy_id)
        user.PharmacyManager.pharmacy_id = pharmacy_obj
        user.save()
        messages.success(request, "Successfully Created Manager")
        return HttpResponseRedirect(reverse("App_Login:login_view"))
    except:
        messages.error(request, "Failed to Create Manager")
        return HttpResponseRedirect(reverse("App_Login:login_view"))


def show_manager_sign_up(request):
    managers = PharmacyAdmin.objects.all()
    return render(request, 'App_Login/manager_sign_up.html', {'managers': managers})



  
'''


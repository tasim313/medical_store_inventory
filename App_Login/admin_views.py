from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from App_Login.models import Admin, Employee, Manager
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Login.decorators import admin_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App_medicine.models import MedicineProduct, Company


@method_decorator([login_required, admin_required], name='dispatch')
class Profile(CreateView):
    model = Admin
    template_name = 'Admin/profile.html'
    fields = ('lic_no', 's_name', 'name', 'contact', 'address')

    def form_valid(self, form):
        admin_obj = form.save(commit=False)
        admin_obj.user = self.request.user
        admin_obj.save()
        messages.success(self.request, 'The profile was created with success! ')
        return redirect('App_Login:index')


def index(request):
    return render(request, 'Admin/HomePage.html')


@login_required
def employee_view(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    employee = Employee.objects.filter(pharmacy_id=admin_obj)
    employee_obj = employee.count()
    diction = {'employee': employee, 'employee_obj': employee_obj}
    return render(request, 'Admin/employee_view.html', context=diction)


@login_required
def manager_view(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    manager = Manager.objects.filter(pharmacy_id=admin_obj)
    manager_obj = manager.count()
    diction = {'manager': manager, 'manager_obj': manager_obj}
    return render(request, 'Admin/manager_view.html', context=diction)



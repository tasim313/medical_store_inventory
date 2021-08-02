from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from App_Login.models import Admin, Employee, Manager
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Login.decorators import admin_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App_medicine.models import Company, MedicineProduct
from App_medicine.forms import AddCompany


@method_decorator([login_required, admin_required], name='dispatch')
class CreateMedicine(CreateView):
    fields = ('company_id', 'name', 'm_type', 'des', 'b_price', 's_price', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no', 'mfg_Lic', 'total_medicine_in_stock')
    model = MedicineProduct
    template_name = 'medicine_product/input_medicine.html'
    context_object_name = 'medicine'

    def form_valid(self, form):
        medicine_create = form.save(commit=False)
        admin_obj = Admin.objects.get(user=self.request.user.id)
        a = Employee.objects.get(user=self.request.user.pharmacy_id)
       # medicine_create.medicine_user = self.request.user
        medicine_create.save()
        return HttpResponseRedirect(reverse('medicine:home'))


@login_required()
def add_company(request, pharmacy_id):
    employee = Employee.objects.get(pharmacy_id=pharmacy_id)
    manager = Manager.objects.get(pharmacy_id=pharmacy_id)
    current_user = request.user
    form = AddCompany(instance=current_user)
    if request.method == 'POST':
        form = AddCompany(request.POST, instance=current_user)
        if form.is_valid():
            form = form.save(commit=False)
            form.admin = current_user
            form.employee = employee
            form.manager = manager
            form.save()
            return HttpResponseRedirect(reverse('App_Login:index'))
    diction = {'form': form}
    return render(request, 'company/create_company.html', context=diction)


@login_required()
def company_view(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    company_list = Company.objects.filter(admin=admin_obj)
    diction = {'company_list': company_list}
    return render(request, "company/company_list.html", context=diction)


@method_decorator([login_required, admin_required], name='dispatch')
class AddCompany(CreateView):
    model = Company
    fields = ('name', 'lic_no', 'address', 'cont_num', 'email', 'description',)
    template_name = 'Admin/add_company.html'

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        admin_obj = Admin.objects.get(user=self.request.user)
        company.pharmacy_id = admin_obj
        manger_obj = Manager.objects.filter(pharmacy_id=admin_obj)
        company.ph_manager_id = Manager.objects.get(pharmacy_id=admin_obj)
        company.ph_employee_id = Employee.objects.get(pharmacy_id=admin_obj).MultipleObjectsReturned
        company.save()
        messages.success(self.request, 'The company information was created with success! ')
        return redirect('App_Login:index')

class CreateCompany(CreateView):
   '''create a view where admin, manager and employee can insert company information in company model'''


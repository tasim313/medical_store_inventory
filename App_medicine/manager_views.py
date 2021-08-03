from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from App_Login.models import Manager
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Login.decorators import manager_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App_medicine.models import Company, MedicineProduct
from App_medicine.forms import AddCompany


@method_decorator([login_required, manager_required], name='dispatch')
class CreateMedicine(CreateView):
    fields = ('company_id', 'name', 'm_type', 'des', 'b_price', 's_price', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no', 'mfg_Lic', 'total_medicine_in_stock')
    model = MedicineProduct
    template_name = 'medicine_product/input_medicine.html'
    context_object_name = 'medicine'

    def form_valid(self, form):
        medicine_create = form.save(commit=False)
        #admin_obj = Admin.objects.get(user=self.request.user.id)
        #a = Employee.objects.get(user=self.request.user.pharmacy_id)
       # medicine_create.medicine_user = self.request.user
        medicine_create.save()
        return HttpResponseRedirect(reverse('medicine:home'))


@login_required
def company_view(request):
    manager_obj = Manager.objects.get(user=request.user.id)
    company_list = Company.objects.filter(ph_manager_id=manager_obj)
    diction = {'company_list': company_list}
    return render(request, "company/company_list.html", context=diction)


@method_decorator([login_required, manager_required], name='dispatch')
class AddCompany(CreateView):
    model = Company
    template_name = 'company/create_company.html'
    fields = ('ph_manager_id',  'name', 'lic_no', 'address', 'cont_num', 'email', 'description',)

    def form_valid(self, form):
        company_obj = form.save(commit=False)
        company_obj.save()
        messages.success(self.request, 'The information was created with success! ')
        return redirect('App_Login:manager_index')
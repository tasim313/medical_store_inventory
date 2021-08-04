from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from App_Login.models import Employee
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Login.decorators import employee_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App_medicine.models import Company, MedicineProduct
from App_medicine.forms import AddCompany


@method_decorator([login_required, employee_required], name='dispatch')
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
    employee_obj = Employee.objects.get(user=request.user.id)
    company_list = Company.objects.filter(ph_employee_id=employee_obj)
    diction = {'company_list': company_list}
    return render(request, "company/employee_company_list.html", context=diction)


@method_decorator([login_required, employee_required], name='dispatch')
class AddCompany(CreateView):
    model = Company
    template_name = 'company/create_company.html'
    fields = ('ph_employee_id',  'name', 'lic_no', 'address', 'cont_num', 'email', 'description',)

    def form_valid(self, form):
        company_obj = form.save(commit=False)
        company_obj.save()
        messages.success(self.request, 'The information was created with success! ')
        return redirect('App_Login:employee_index')


@method_decorator([login_required, employee_required], name='dispatch')
class UpdateCompany(UpdateView):
    model = Company
    fields = ('ph_employee_id', 'name', 'lic_no', 'address', 'cont_num', 'email', 'description')
    template_name = 'company/employee_update_company.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('medicine:employee_company_view', kwargs={})


@method_decorator([login_required, employee_required], name='dispatch')
class CompanyDelete(DeleteView):
    context_object_name = 'company'
    model = Company
    success_url = reverse_lazy('medicine:employee_company_view')
    template_name = 'company/employee_Delete_company.html'


@login_required
@employee_required
def search_company(request):
    employ_obj = Employee.objects.get(user=request.user.id)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Company.objects.filter(name__icontains=search, ph_employee_id=employ_obj)
    return render(request, 'company/search_company.html', context={'search': search, 'result': result})

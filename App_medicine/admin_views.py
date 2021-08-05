from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from App_Login.models import Admin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Login.decorators import admin_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App_medicine.models import Company, MedicineProduct
from App_medicine.forms import AddCompany


@login_required()
def company_view(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    company_list = Company.objects.filter(pharmacy_id=admin_obj)
    diction = {'company_list': company_list}
    return render(request, "company/company_list.html", context=diction)


@method_decorator([login_required, admin_required], name='dispatch')
class AddCompany(CreateView):
    model = Company
    template_name = 'company/create_company.html'
    fields = ('pharmacy_id',  'name', 'lic_no', 'address', 'cont_num', 'email', 'description',)

    def form_valid(self, form):
        company_obj = form.save(commit=False)
        company_obj.save()
        messages.success('This information was created with success! ')
        return redirect('App_Login:index')


@method_decorator([login_required, admin_required], name='dispatch')
class UpdateCompany(UpdateView):
    model = Company
    fields = ('pharmacy_id', 'name', 'lic_no', 'address', 'cont_num', 'email', 'description')
    template_name = 'company/update_company.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('medicine:company_view', kwargs={})


@method_decorator([login_required, admin_required], name='dispatch')
class CompanyDelete(DeleteView):
    context_object_name = 'company'
    model = Company
    success_url = reverse_lazy('medicine:company_view')
    template_name = 'company/Delete_company.html'


@login_required
@admin_required
def search_company(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Company.objects.filter(name__icontains=search, pharmacy_id=admin_obj)
    return render(request, 'company/search_company.html', context={'search': search, 'result': result})


@method_decorator([login_required, admin_required], name='dispatch')
class CreateMedicine(CreateView):
    fields = ('company_id', 'pharmacy_id', 'name', 'm_type', 'des', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no',
              'mfg_Lic', 'total_quantity', 'issued_quantity', 'received_quantity', 'buy_price', 'unit_price')
    model = MedicineProduct
    template_name = 'medicine_product/input_medicine.html'
    context_object_name = 'medicine'

    def form_valid(self, form):
        medicine_create = form.save(commit=False)
        medicine_create.save()
        messages.success(self.request, 'This medicine was created with success! ')
        return HttpResponseRedirect(reverse('App_Login:index'))


@login_required
@admin_required
def medicine_view(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    medicine_list = MedicineProduct.objects.filter(pharmacy_id=admin_obj)
    diction = {'medicine_list': medicine_list}
    return render(request, 'medicine_product/product_view.html', context=diction)


@method_decorator([login_required, admin_required], name='dispatch')
class UpdateMedicine(UpdateView):
    model = MedicineProduct
    fields = ('company_id', 'pharmacy_id', 'name', 'm_type', 'des', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no',
              'mfg_Lic', 'total_quantity', 'issued_quantity', 'received_quantity', 'buy_price', 'unit_price')
    template_name = 'medicine_product/update_medicine.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('medicine:admin_medicine_view', kwargs={})


@method_decorator([login_required, admin_required], name='dispatch')
class MedicineDelete(DeleteView):
    context_object_name = 'medicine'
    model = MedicineProduct
    success_url = reverse_lazy('medicine:admin_medicine_view')
    template_name = 'medicine_product/delete_medicine.html'


@login_required
@admin_required
def search_medicine(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = MedicineProduct.objects.filter(name__icontains=search, pharmacy_id=admin_obj)
    return render(request, 'medicine_product/search_medicine.html', context={'search': search, 'result': result})


@login_required
@admin_required
def search_medicine_expire_date(request):
    admin_obj = Admin.objects.get(user=request.user.id)
    if request.method == 'GET':
        search = request.GET.get('search',)
        result = MedicineProduct.objects.filter(expire_date__exact=search, pharmacy_id=admin_obj)
    return render(request, 'medicine_product/expire_medicine.html', context={'search': search, 'result': result})

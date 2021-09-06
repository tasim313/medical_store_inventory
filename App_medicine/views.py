'''''
from django.shortcuts import render, HttpResponseRedirect
from .models import MedicineProduct, Company
from .forms import MedicineForm
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
# Create your views here.


def medicine_view(request):
    medicine_list = MedicineProduct.objects.all()
    diction = {'medicine_list': medicine_list}
    return render(request, 'medicine_product/product_view.html', context=diction)


class CreateMedicine(CreateView):
    fields = ('company_id', 'name', 'm_type', 'des', 'b_price', 's_price', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no', 'mfg_Lic', 'total_medicine_in_stock')
    model = MedicineProduct
    template_name = 'medicine_product/input_medicine.html'
    context_object_name = 'medicine'

    def form_valid(self, form):
        medicine_create = form.save(commit=False)
       # medicine_create.medicine_user = self.request.user
        medicine_create.save()
        return HttpResponseRedirect(reverse('medicine:home'))


class UpdateMedicine(UpdateView):
    model = MedicineProduct
    fields = ('company_id', 'name', 'm_type', 'des', 'b_price', 's_price', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no', 'mfg_Lic', 'total_medicine_in_stock')
    template_name = 'medicine_product/update_medicine.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('medicine:home', kwargs={})


class MedicineDelete(DeleteView):
    context_object_name = 'medicine'
    model = MedicineProduct
    success_url = reverse_lazy('medicine:home')
    template_name = 'medicine_product/delete_medicine.html'


def search_medicine(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = MedicineProduct.objects.filter(name__icontains=search)
    return render(request, 'medicine_product/search_medicine.html', context={'search': search, 'result': result})


def search_medicine_expire_date(request):
    if request.method == 'GET':
        search = request.GET.get('search',)
        result = MedicineProduct.objects.filter(expire_date__exact=search)
    return render(request, 'medicine_product/expire_medicine.html', context={'search': search, 'result': result})

'''''

from django.shortcuts import render, HttpResponseRedirect


def main_home_page(request):
    return render(request, 'MainTemplate.html')
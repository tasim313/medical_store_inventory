from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from App_Login.models import Employee
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Login.decorators import employee_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App_medicine.models import Company, MedicineProduct, Sale
from App_medicine.forms import AddForm, EmployeeSaleForm


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
        return redirect('medicine:employee_company_view')


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


@method_decorator([login_required, employee_required], name='dispatch')
class CreateMedicine(CreateView):
    fields = ('company_id', 'ph_employee_id', 'name', 'm_type', 'des', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no',
    'mfg_Lic', 'total_quantity', 'issued_quantity', 'received_quantity', 'buy_price', 'unit_price')
    model = MedicineProduct
    template_name = 'medicine_product/input_medicine.html'
    context_object_name = 'medicine'

    def form_valid(self, form):
        medicine_create = form.save(commit=False)
        medicine_create.save()
        return HttpResponseRedirect(reverse('medicine:employee_medicine_view'))


@login_required
@employee_required
def medicine_view(request):
    employee_obj = Employee.objects.get(user=request.user.id)
    medicine_list = MedicineProduct.objects.filter(ph_employee_id=employee_obj)
    diction = {'medicine_list': medicine_list}
    return render(request, 'medicine_product/employee_product_view.html', context=diction)


@method_decorator([login_required, employee_required], name='dispatch')
class UpdateMedicine(UpdateView):
    model = MedicineProduct
    fields = ('company_id', 'ph_manager_id', 'name', 'm_type', 'des', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no',
    'mfg_Lic', 'total_quantity', 'issued_quantity', 'received_quantity', 'buy_price', 'unit_price')
    template_name = 'medicine_product/update_medicine.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('medicine:employee_medicine_view', kwargs={})


@method_decorator([login_required, employee_required], name='dispatch')
class MedicineDelete(DeleteView):
    context_object_name = 'medicine'
    model = MedicineProduct
    success_url = reverse_lazy('medicine:employee_medicine_view')
    template_name = 'medicine_product/employee_delete_medicine.html'


@login_required
@employee_required
def search_medicine(request):
    employee_obj = Employee.objects.get(user=request.user.id)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = MedicineProduct.objects.filter(name__icontains=search, ph_employee_id=employee_obj)
    return render(request, 'medicine_product/search_medicine.html', context={'search': search, 'result': result})


@login_required
@employee_required
def search_medicine_expire_date(request):
    employee_obj = Employee.objects.get(user=request.user.id)
    if request.method == 'GET':
        search = request.GET.get('search', )
        result = MedicineProduct.objects.filter(expire_date__exact=search, ph_employee_id=employee_obj)
    return render(request, 'medicine_product/expire_medicine.html', context={'search': search, 'result': result})


@login_required
@employee_required
def receipt(request):
    employee_obj = Employee.objects.get(user=request.user.id)
    sales = Sale.objects.filter(ph_employee_id=employee_obj)
    #sales = new_sale.order_by('-id')
    #sale = Sale.objects.all().order_by('-id')
    #sales = sale.filter(pharmacy_id=admin_obj).order_by('-id')
    return render(request, 'Sales/receipt.html', {'sales': sales, })


@login_required
@employee_required
def all_sales(request):
    employee_obj = Employee.objects.get(user=request.user.id)
    #sale = Sale.objects.all()
    sales = Sale.objects.filter(ph_employee_id=employee_obj)
    total = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'Sales/all_sales.html', {'sales': sales, 'total': total, 'change': change, 'net': net, })


@login_required
@employee_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id=receipt_id)
    return render(request, 'Sales/receipt_detail.html', {'receipt': receipt})


@login_required
@employee_required
def issue_item(request, pk):
    issued_item = MedicineProduct.objects.get(id=pk)
    sales_form = EmployeeSaleForm(request.POST)

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.employee = issued_item.ph_employee_id
            new_sale.save()
            # To keep track of the stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('medicine:employee_sell_product')

    return render(request, 'Sales/issue_item.html', {'sales_form': sales_form, })


@login_required
@employee_required
def add_to_stock(request, pk):
    issued_item = MedicineProduct.objects.get(id=pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            return redirect('medicine:employee_sell_product')

    return render(request, 'Sales/add_to_stock.html', {'form': form})


@login_required
@employee_required
def sell_product_detail(request):
    employee_obj = Employee.objects.get(user=request.user.id)
    product_list = MedicineProduct.objects.filter(ph_employee_id=employee_obj)
    return render(request, 'Employee/product_detail.html', {'product_list': product_list})

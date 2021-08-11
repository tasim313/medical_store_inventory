'''''
from django import forms
from .models import MedicineProduct


class MedicineForm(forms.ModelForm):
    class Meta:
        model = MedicineProduct
        fields = ('company_id', 'name', 'm_type', 'des', 'b_price', 's_price', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no', 'mfg_Lic')

'''''

from django import forms

from App_medicine.models import MedicineProduct, Sale


class AddForm(forms.ModelForm):
    class Meta:
        model = MedicineProduct
        fields = ['received_quantity']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('pharmacy_id', 'quantity', 'amount_received', 'issued_to',)


class ManagerSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('ph_manager_id', 'quantity', 'amount_received', 'issued_to',)


class EmployeeSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('ph_employee_id', 'quantity', 'amount_received', 'issued_to',)

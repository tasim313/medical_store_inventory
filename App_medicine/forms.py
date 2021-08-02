'''''
from django import forms
from .models import MedicineProduct


class MedicineForm(forms.ModelForm):
    class Meta:
        model = MedicineProduct
        fields = ('company_id', 'name', 'm_type', 'des', 'b_price', 's_price', 'b_no', 's_no', 'mfg_date', 'expire_date', 'dar_no', 'mfg_Lic')

'''''

from django import forms

from App_medicine.models import Company


class AddCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'lic_no', 'address', 'cont_num', 'email', 'description',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        if commit:
            user.save()
        return user





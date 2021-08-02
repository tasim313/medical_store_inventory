'''''
from django import forms
from App_Login.models import PharmacyAdmin, PharmacyManager, Employee
from App_Login.models import CustomUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')


class AdminInfoForm(forms.ModelForm):
    class Meta:
        model = PharmacyAdmin
        fields = ('lic_no', 's_name', 'name', 'contact', 'address')


class ManagerInfoForm(forms.ModelForm):
    class Meta:
        model = PharmacyManager
        fields = ('pharmacy_id', 'name', 'contact', 'address')


class EmployeeInfoForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('pharmacy_id', 'name', 'contact', 'address')

'''''
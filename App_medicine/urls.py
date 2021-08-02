'''''
from django.urls import path
from . import views
from . import company_views
from .views import CreateMedicine, UpdateMedicine, MedicineDelete, search_medicine, search_medicine_expire_date
from .company_views import CreateCompany, company_view, UpdateCompany, CompanyDelete, search_company
app_name = 'medicine'

urlpatterns = [
    path('', views.medicine_view, name='home'),
    path('input_medicine/', views.CreateMedicine.as_view(), name='input'),
    path('update/<pk>/', views.UpdateMedicine.as_view(), name='update_medicine'),
    path('delete_medicine/<pk>/', views.MedicineDelete.as_view(), name='delete_medicine'),
    path('company_list/', company_views.company_view, name='company_list'),
    path('insert_company/', company_views.CreateCompany.as_view(), name='insert_company'),
    path('update_company/<pk>/', company_views.UpdateCompany.as_view(), name='update_company'),
    path('delete_company/<pk>/', company_views.CompanyDelete.as_view(), name='delete_company'),
    path('search/', views.search_medicine, name='search'),
    path('search_company/', company_views.search_company, name='search_company'),
    path('expire_date/', views.search_medicine_expire_date, name='expire_date'),
]

'''

from django.urls import path
from . import admin_views

app_name = 'medicine'

urlpatterns = [
    path('admin/add_company/', admin_views.add_company, name='add_company'),
    path('admin/view_company', admin_views.company_view, name='company_view'),
    path('admin/company/', admin_views.AddCompany.as_view(), name='company'),
]
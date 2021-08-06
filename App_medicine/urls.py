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
from . import admin_views, manager_views, employee_views

app_name = 'medicine'

urlpatterns = [
    path('admin/add_company/', admin_views.AddCompany.as_view(), name='add_company'),
    path('admin/view_company', admin_views.company_view, name='company_view'),
    path('manger/add_company/', manager_views.AddCompany.as_view(), name='manager_add_company'),
    path('manager/view_company/', manager_views.company_view, name='manager_company_view'),
    path('employee/add_company/', employee_views.AddCompany.as_view(), name='employee_add_company'),
    path('employee/view_company/', employee_views.company_view, name='employee_company_view'),
    path('update_company/<pk>/', admin_views.UpdateCompany.as_view(), name='admin_update_company'),
    path('delete_company/<pk>/', admin_views.CompanyDelete.as_view(), name='admin_delete_company'),
    path('search_company/', admin_views.search_company, name='admin_search_company'),
    path('manager/update_company/<pk>/', manager_views.UpdateCompany.as_view(), name='manager_update_company'),
    path('manager/delete_company/<pk>/', manager_views.CompanyDelete.as_view(), name='manager_delete_company'),
    path('manager/search_company/', manager_views.search_company, name='manager_search_company'),
    path('employee/update_company/<pk>/', employee_views.UpdateCompany.as_view(), name='employee_update_company'),
    path('employee/delete_company/<pk>/', employee_views.CompanyDelete.as_view(), name='employee_delete_company'),
    path('employee/search_company/', employee_views.search_company, name='employee_search_company'),
    path('admin/add_medicine/', admin_views.CreateMedicine.as_view(), name='admin_add_medicine'),
    path('admin/medicine_view', admin_views.medicine_view, name='admin_medicine_view'),
    path('admin/update/<pk>/', admin_views.UpdateMedicine.as_view(), name='admin_update_medicine'),
    path('admin/delete_medicine/<pk>/', admin_views.MedicineDelete.as_view(), name='admin_delete_medicine'),
    path('admin/search/', admin_views.search_medicine, name='admin_search_medicine'),
    path('admin/expire_date/', admin_views.search_medicine_expire_date, name='admin_view_expire_date'),
    path('manager/medicine_view', manager_views.medicine_view, name='manager_medicine_view'),
    path('manager/add_medicine/', manager_views.CreateMedicine.as_view(), name='manager_add_medicine'),
    path('manager/update/<pk>/', manager_views.UpdateMedicine.as_view(), name='manager_update_medicine'),
    path('manager/delete_medicine/<pk>/', manager_views.MedicineDelete.as_view(), name='manager_delete_medicine'),
    path('manager/search/', manager_views.search_medicine, name='manager_search_medicine'),
    path('manager/expire_date/', manager_views.search_medicine_expire_date, name='manager_view_expire_date'),
    path('employee/medicine_view', employee_views.medicine_view, name='employee_medicine_view'),
    path('employee/add_medicine/', employee_views.CreateMedicine.as_view(), name='employee_add_medicine'),
    path('employee/update/<pk>/', employee_views.UpdateMedicine.as_view(), name='employee_update_medicine'),
    path('employee/delete_medicine/<pk>/', employee_views.MedicineDelete.as_view(), name='employee_delete_medicine'),
    path('employee/search/', employee_views.search_medicine, name='employee_search_medicine'),
    path('employee/expire_date/', employee_views.search_medicine_expire_date, name='employee_view_expire_date'),
]
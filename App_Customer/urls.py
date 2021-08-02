from django.urls import path
from . import views
from .views import CreateCustomer, CustomerUpdate, CustomerDelete


app_name = 'App_Customer'


urlpatterns = [
    path('customer_list/', views.customer_list_info, name='customer_list'),
    path('customer_insert/', views.CreateCustomer.as_view(), name='customer_create'),
    path('update_customer/<pk>/', views.CustomerUpdate.as_view(), name='update_customer'),
    path('delete_customer/<pk>/', views.CustomerDelete.as_view(), name='delete_customer'),
    path('search_customer/', views.customer_info_search, name='customer_search'),
]

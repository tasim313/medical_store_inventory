from django.urls import path
from . import views
app_name = 'App_bill'

urlpatterns = [
    path('sells_view/', views.sell_medicine, name='sell_medicine'),
    path('add_to_bill/<pk>/', views.add_to_bill, name='add_to_bill'),
    path('bill/', views.bill_view, name='bill'),
    path('remove/<pk>/', views.remove_from_bill, name='remove'),
    path('increase_bill/<pk>/', views.increase_bill, name='increase_bill'),
    path('decrease_bill/<pk>/', views.decrease_bill, name='decrease_bill'),
]
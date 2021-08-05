'''''
from django.shortcuts import render, get_object_or_404, redirect

import App_Customer.models
from App_medicine.models import MedicineProduct
from App_Customer.models import Customer
from App_bill.models import Bill, Order
from django.contrib import messages
# Create your views here.


def sell_medicine(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = MedicineProduct.objects.filter(name__icontains=search)
    return render(request, 'bill/sell_medicine.html', context={'search': search, 'result': result})


def add_to_bill(request, pk):
    item = get_object_or_404(MedicineProduct, pk=pk)
    customer_id = request.POST.get('customer_id')
    order_item = Bill.objects.get_or_create(item=item, customer_id=customer_id, purchased=False)
    order_qs = Order.objects.filter(customer_id=customer_id, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated.")
            return redirect("App_bill:sell_medicine")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added to this bill.")
            return redirect("App_bill:sell_medicine")
    else:
        order = Order(customer_id=customer_id)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item was added to this bill.")
        return redirect("App_bill:sell_medicine")


def bill_view(request):
    bills = Bill.objects.filter(customer_id=Bill.customer_id, purchased=False)
    orders = Order.objects.filter(customer_id=Bill.customer_id, ordered=False)
    if bills.exists() and orders.exists():
        order = orders[0]
        return render(request, 'bill/bill.html', context={'order': order, 'bills': bills})
    else:
        messages.warning(request, "Customer don't have any item in  bill !")
        return redirect('App_bill:sell_medicine')


def remove_from_bill(request, pk):
    item = get_object_or_404(MedicineProduct, pk=pk)
    order_qs = Order.objects.filter(customer_id=Bill.customer_id, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Bill.objects.filter(item=item, customer_id=Bill.customer_id, purchased=False)
            order_item = order_item[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This Item was remove from this bill")
            return redirect('App_bill:bill')
        else:
            messages.info(request, 'This Item was not in your cart.')
            return redirect('App_bill:sell_medicine')
    else:
        messages.info(request, "Customer don't have an active order")
        return redirect('App_bill:sell_medicine')


def increase_bill(request, pk):
    item = get_object_or_404(MedicineProduct, pk=pk)
    order_qs = Order.objects.filter(customer_id=Bill.customer_id, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Bill.objects.filter(item=item, customer_id=Bill.customer_id, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("App_bill:bill")
        else:
            messages.info(request, f"{item.name} is not in this bill")
            return redirect("App_bill:sell_medicine")
    else:
        messages.info(request, "You don't have an active order")
        return redirect("App_bill:sell_medicine")


def decrease_bill(request, pk):
    item = get_object_or_404(MedicineProduct, pk=pk)
    order_qs = Order.objects.filter(customer_id=Bill.customer_id, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Bill.objects.filter(item=item, customer_id=Bill.customer_id, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.warning(request, f"{item.name} quantity has been updated")
                return redirect('App_bill:bill')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.name} item has been removed from this bill")
                return redirect("App_bill:bill")
        else:
            messages.info(request, f"{item.name} is not in this bill.")
            return redirect('App_bill:sell_medicine')
    else:
        messages.info(request, "You don't have an active order")
        return redirect('App_bill:sell_medicine')
'''''
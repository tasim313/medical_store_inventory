from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from App_Customer.models import Customer
from django.urls import reverse, reverse_lazy
# Create your views here.


def customer_list_info(request):
    customer_list = Customer.objects.all()
    return render(request, 'customer/customer_list.html', context={'customer_list': customer_list})


class CreateCustomer(CreateView):
    model = Customer
    template_name = 'customer/create_customer.html'
    fields = ('name', 'address', 'contact', 'email')

    def form_valid(self, form):
        customer_create = form.save(commit=False)
        customer_create.save()
        return HttpResponseRedirect(reverse('App_Customer:customer_list'))


class CustomerUpdate(UpdateView):
    model = Customer
    template_name = 'customer/update_customer_info.html'
    fields = ('name', 'address', 'contact', 'email')

    def get_success_url(self):
        return reverse_lazy('App_Customer:customer_list')


class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customer/Delete_customer_info.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('App_Customer:customer_list')


def customer_info_search(request):
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Customer.objects.filter(name__icontains=search)
        return render(request, 'customer/search_customer_info.html', context={'search': search, 'result': result})
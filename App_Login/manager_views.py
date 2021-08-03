from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from App_Login.models import Manager, Employee
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Login.decorators import manager_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@method_decorator([login_required, manager_required], name='dispatch')
class Profile(CreateView):
    model = Manager
    template_name = 'manager/profile.html'
    fields = ('pharmacy_id', 'name', 'contact', 'address')

    def form_valid(self, form):
        manager_obj = form.save(commit=False)
        manager_obj.user = self.request.user
        manager_obj.save()
        messages.success(self.request, 'The profile was created with success! ')
        return redirect('App_Login:manager_index')


def index(request):
    return render(request, 'manager/manager_home_page.html')



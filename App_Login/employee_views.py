from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from App_Login.models import Employee
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Login.decorators import employee_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@method_decorator([login_required, employee_required], name='dispatch')
class EmployeeProfile(CreateView):
    model = Employee
    template_name = 'Employee/profile.html'
    fields = ('pharmacy_id', 'name', 'contact', 'address')

    def form_valid(self, form):
        employee_obj = form.save(commit=False)
        employee_obj.user = self.request.user
        employee_obj.save()
        messages.success(self.request, 'The profile was created with success! ')
        return redirect('App_Login:employee_index')


def index(request):
    return render(request, 'Employee/employee_home_page.html')
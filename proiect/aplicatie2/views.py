from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import Companies


class CompanyView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'


class CreateCompanyView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = ["name", "company_type", "website", "active", "location"]
    template_name = 'aplicatie2/companies_form.html'


    def get_success_url(self):
        return reverse('companies:listare')


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = ["name", "company_type", "website", "active"]
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('companies:listare')

@login_required
def delete_company(request, pk):
    Companies.objects.filter(id=pk).update(active=0)
    return redirect('companies:listare')

@login_required
def activate_company(request, pk):
    Companies.objects.filter(id=pk).update(active=1)
    return redirect('companies:listare')

class CompanyInactiveView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(CompanyInactiveView, self).get_context_data( *args, **kargs)
        data['companies_list'] = self.model.objects.filter(active=0)
        return data
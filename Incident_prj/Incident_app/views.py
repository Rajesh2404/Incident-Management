from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import IncidentCreateForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Incidence

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'Incident_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('incidents')


class RegisterPage(FormView):
    template_name = 'Incident_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('incidents')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

class IncidentList(LoginRequiredMixin, ListView):
    model = Incidence
    context_object_name = 'incidents'

class IncidentDetail(LoginRequiredMixin, DetailView):
    model = Incidence
    context_object_name = 'incident'
    template_name = 'Incident_app/incident_detail.html'

class IncidentCreate(LoginRequiredMixin, CreateView, FormView):
    model = Incidence
    form_class = IncidentCreateForm
    success_url = reverse_lazy('incidents')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IncidentCreate, self).form_valid(form)

class IncidentDelete(LoginRequiredMixin, DeleteView):
    model = Incidence
    context_object_name = 'incident'
    success_url = reverse_lazy('incidents')
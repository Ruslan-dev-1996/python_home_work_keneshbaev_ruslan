from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TypeForm
from webapp.models import Type
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .base_views import ListView, UpdateView, DeleteView


class TypeView(ListView):
    template_name = 'type/type_view.html'
    model = Type
    context_key = 'types'




class TypeCreateView(CreateView):
    template_name = 'type/create_type.html'
    model = Type
    fields = ['name']

    def get_success_url(self):
        return reverse('type_view')



class TypeUpdateView(UpdateView):
    model = Type
    template_name = 'type/update_type.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_redirect_url(self):
        return reverse('type_view')



class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/delete_type.html'
    context_object_name = 'type'
    error = 'error_type.html'

    def get_redirect_url(self):
        return reverse('type_view')
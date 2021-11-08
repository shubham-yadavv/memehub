from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from .models import Index
from django.views.generic.list import ListView

class Index(ListView):
    model = Index
    paginate_by = 10
    context_object_name = 'index'
    template_name = 'index.html'
    ordering = ['-date']
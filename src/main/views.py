from django.shortcuts import render
from django.contrib import messages
from .models import (
  UserProfile,
  Blog,
  Portfolio,
  Certificate
)
from django.contrib.auth import get_user_model

from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = "main/index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    certificates = Certificate.objects.filter(is_active=True)
    blogs = Blog.objects.filter(is_active=True)
    portfolio = Portfolio.objects.filter(is_active=True)

    context["me"] = get_user_model().objects.first()
    context["certificates"] = certificates
    context["blogs"] = blogs
    context["portfolio"] = portfolio
    
    return context
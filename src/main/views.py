from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from braces import views

from .models import (
  UserProfile,
  Blog,
  Portfolio,
  Certificate,
  ContactProfile
)
from django.contrib.auth import get_user_model

from django.views import generic

from .forms import ContactForm

# Create your views here.
class IndexView(generic.TemplateView):
  template_name = "main/index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    certificates = Certificate.objects.filter(is_active=True)
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')[0:4]
    portfolio = Portfolio.objects.filter(is_active=True).filter(is_featured=True)

    context["me"] = get_user_model().objects.first()
    context["certificates"] = certificates
    context["blogs"] = blogs
    context["portfolio"] = portfolio
    
    return context

class ContactView(generic.FormView):
  template_name = "main/contact.html"
  form_class = ContactForm
  success_url = "/"

  def form_valid(self, form):
    form.save()
    messages.success(self.request, "Thank you. We will be in touch soon.")
    return super().form_valid(form)

class ContactMessageView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, generic.ListView):
  model = ContactProfile
  template_name = "main/contact-profile.html"
  paginate_by = 20

  def get_queryset(self):
    return super().get_queryset().order_by("-timestamp")

@login_required
@user_passes_test(lambda u: u.is_superuser)
def toggle_message_read_view(request, id):
  message = get_object_or_404(ContactProfile, id=id)

  message.has_been_viewed = not message.has_been_viewed

  message.save()

  return JsonResponse({
    'is_toggled': True
  })



class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True).order_by('-date')

class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
  model = Blog
  template_name = "main/blog.html"
  paginate_by = 10

  def get_queryset(self):
    return super().get_queryset().filter(is_active=True).order_by('-created_at')

class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"

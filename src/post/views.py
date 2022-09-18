from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from braces import views

from .forms import BlogForm

from main.models import (
  Blog,
  Portfolio
)

# Create your views here.
class CreateBlogView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, CreateView):
  model = Blog
  form_class = BlogForm
  template_name = 'post/blog.html'
  success_url = '/blog/'

  def form_valid(self, form):
    obj = form.save(commit=False)
    obj.author = self.request.user
    return super().form_valid(form)

class UpdateBlogView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, UpdateView):
  model = Blog
  form_class =BlogForm
  template_name = 'post/blog.html'
  success_url = '/blog/'
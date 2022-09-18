from django import forms

from main.models import Blog

class BlogForm(forms.ModelForm):

  title = forms.CharField(max_length=200, required=True)
  description = forms.CharField(max_length=500, required=True)
  image = forms.ImageField(required=False)

  class Meta:
    model = Blog
    fields = ['title', 'description', 'body', 'image', 'tags', 'is_active']
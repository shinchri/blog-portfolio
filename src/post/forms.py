from django import forms

from main.models import Blog, Portfolio

from .widgets import DateTimePickerInput

class BlogForm(forms.ModelForm):

  title = forms.CharField(max_length=200, required=True)
  description = forms.CharField(max_length=500, required=True)
  image = forms.ImageField(required=False)

  class Meta:
    model = Blog
    fields = ['title', 'description', 'body', 'image', 'tags', 'is_active']

class PortfolioForm(forms.ModelForm):

  name = forms.CharField(max_length=200, required=True)
  description = forms.CharField(max_length=500, required=True)
  image = forms.ImageField(required=False)
  date = forms.DateTimeField(required=True, widget=DateTimePickerInput())

  class Meta:
    model = Portfolio
    fields = ['name', 'date', 'description', 'body', 'image', 'tags', 'is_active', 'is_featured']
    widgets = {
      'date': DateTimePickerInput(),
    }
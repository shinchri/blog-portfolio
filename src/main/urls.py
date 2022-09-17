from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
  path('', views.IndexView.as_view(), name="home"),
  path('contact/', views.ContactView.as_view(), name="contact"),
  path('blog/', views.BlogView.as_view(), name="blogs"),
]
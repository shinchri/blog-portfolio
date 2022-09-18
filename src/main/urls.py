from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
  path('', views.IndexView.as_view(), name="home"),
  path('contact/', views.ContactView.as_view(), name="contact"),
  path('messages/', views.ContactMessageView.as_view(), name="messages"),
  path('message/toggle/<int:id>/', views.toggle_message_read_view, name="toggle"),
  path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
  path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
  path('blog/', views.BlogView.as_view(), name="blogs"),
  path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
]
from django.urls import path
from .views import CreateBlogView, UpdateBlogView, CreatePortfolioView, UpdatePortfolioView

app_name = "post"

urlpatterns = [
  path('blog/add/', CreateBlogView.as_view(), name="create-blog"),
  path('blog/<slug:slug>/', UpdateBlogView.as_view(), name="update-blog"),
  path('portfolio/add/', CreatePortfolioView.as_view(), name="create-portfolio"),
  path('portfolio/<slug:slug>/', UpdatePortfolioView.as_view(), name="update-portfolio"),

]
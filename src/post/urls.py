from django.urls import path
from .views import CreateBlogView, UpdateBlogView

app_name = "post"

urlpatterns = [
  path('blog/add/', CreateBlogView.as_view(), name="create-blog"),
  path('blog/<slug:slug>', UpdateBlogView.as_view(), name="update-blog"),
]
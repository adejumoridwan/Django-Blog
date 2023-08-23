from django.urls import include, path
from django.views.generic import TemplateView
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

from . import views

blog_patterns = [
    path("", TemplateView.as_view(template_name='blog_home.html'),
         name='blog_home'),
    path("blogs/", views.BlogListView.as_view(), name="blog_list"),
    path("blogger/<int:pk>/", views.AuthorDetailView.as_view(), name="author_detail"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("bloggers/", views.AuthorListView.as_view(), name="author_list"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout')
]

urlpatterns = [
    path("", include(blog_patterns)),
]

# path("/accounts/<standard-urls"),
# path("/admin/<standard-urls>"),

from django.urls import reverse_lazy
from django.urls import reverse
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

from blog.models import Blog, Author, Comment

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'login_form.html'


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    paginate = 5
    template_name = "blog_list.html"

    def get_queryset(self):
        return Blog.objects.all().order_by('-date')


class BlogDetailView(LoginRequiredMixin, DetailView, CreateView):
    model = Blog
    template_name = "blog_detail.html"
    context_object_name = 'blog'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.post = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.kwargs['pk']})


class AuthorListView(LoginRequiredMixin, ListView):
    model = Author
    model = Comment
    paginate = 5
    template_name = "author_list.html"

    def get_queryset(self):
        return Author.objects.all().order_by('user__first_name')


class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    template_name = "author_detail.html"
    context_object_name = 'author'

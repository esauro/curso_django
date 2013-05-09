# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from blog.models import Post


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
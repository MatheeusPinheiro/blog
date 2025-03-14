from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.order_by('-data_publicacao')[::-1]
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)

def post_detail(request, pk):
    
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
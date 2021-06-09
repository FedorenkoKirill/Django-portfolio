from django.shortcuts import render
from .models import Blog

def index(request):
    posts = Blog.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

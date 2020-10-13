from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
def blog(request):
    return render(request, 'blog.html', {  } )
def post_detail(request):
    return render(request, 'post_detail.html', {  } )
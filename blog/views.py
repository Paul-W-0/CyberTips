from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
def blog(request):
    slug_query = Post.objects.all()
    queryset = Post.objects.all().order_by('-published_on')
    return render(request, 'blog.html', { 'queryset':queryset, } )
def about(request):
    return render(request, 'about.html', {  } )
def post_detail(request, slug):
    slug_from_post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', { 'slug_from_post':slug_from_post, } )
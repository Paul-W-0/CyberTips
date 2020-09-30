from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
def blog(request):
    return render(request, 'blog.html', {  } )

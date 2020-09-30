from django.urls import path
from . import views
url_patterns = [
    path('blog/', views.blog, name='blog'),
]
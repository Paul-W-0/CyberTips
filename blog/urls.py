from django.urls import path, include
from . import views
urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('post/slug:slug/', views.post_detail, name='post_detail'),
]
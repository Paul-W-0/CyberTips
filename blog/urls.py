from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]
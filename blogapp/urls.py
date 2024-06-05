from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('index/', views.index_page, name='index_page'),
    path('blog_list/', views.blog_list, name='blog_list'),

]
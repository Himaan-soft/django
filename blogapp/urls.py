from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('main/', views.main_page),
    path('blog_list/', views.blog_list),

]
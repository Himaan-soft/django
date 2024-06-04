from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Blog 
from .serializers import BlogSerializers

@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.all()
    serializers =  BlogSerializers(blogs, many=True)

    return Response(serializers.data)

def hello_world(request):
    return HttpResponse('Hello World, !!')

def main_page(request):
    return render(request, 'main.html', {'name' : 'Laxmi Yadav'})

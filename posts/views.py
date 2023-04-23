from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer,PostSerializer
# ,CommentSerializer
from .models import Author,Post,Comment
# Create your views here.
def say_hello(request):
    return render(request,'index.html',{'name':'Waqar'})

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class CommentViewSet(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

    
def ViewSetTester(request):
    return HttpResponse('ok')
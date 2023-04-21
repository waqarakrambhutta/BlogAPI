from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer
from .models import Author
# Create your views here.
def say_hello(request):
    return render(request,'index.html',{'name':'Waqar'})

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


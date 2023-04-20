from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def say_hello(request):
    return render(request,'index.html',{'name':'Waqar'})

@api_view()
def author_list(request):
    return Response('ok')
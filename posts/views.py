from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer
from .models import Author
# Create your views here.
def say_hello(request):
    return render(request,'index.html',{'name':'Waqar'})

class AuthorViewSet(ModelViewSet):
    http_method_names = ['get','post','patch','delete','put','update','head','options']
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_serializer_context(self):
        return {'author_id':self.kwargs['pk']}

def AutherViewset(request):
    queryset= Author.objects.all()
    serializer = AuthorSerializer(queryset,many=True)
    return HttpResponse(serializer.data)

    
def ViewSetTester(request):
    return HttpResponse('ok')
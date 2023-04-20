from django.shortcuts import render


# Create your views here.
def say_hello(request):
    return render(request,'index.html',{'name':'Waqar'})

def author_list(request):
    return 
from django.urls import path,include
from .views import say_hello
from . import views


urlpatterns = [
    path('hello/',say_hello),
    path('author/',views.author_list)
]
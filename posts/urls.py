from django.urls import path,include
from .views import say_hello
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'author',views.AuthorViewSet)


urlpatterns = [
    path('hello/',say_hello),
    # path('author/',views.author_list)
]
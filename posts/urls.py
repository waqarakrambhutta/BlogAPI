from django.urls import path,include
from .views import say_hello
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('author',views.AuthorViewSet)



urlpatterns = router.urls + [
    path('hello/',say_hello),
    # path('author/',views.AutherViewset),
] 
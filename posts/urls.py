from django.urls import path,include
from .views import say_hello
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('author',views.AuthorViewSet)
router.register('posts',views.PostViewSet)
router.register('comments',views.CommentViewSet)

# author_router = routers.NestedDefaultRouter(
#     router,
#     'author',
#     lookup='product')
# author_router.register('posts',views.PostSerializer,basename='post')

urlpatterns = router.urls + [path('hello/',say_hello)] 





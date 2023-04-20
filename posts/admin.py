from django.contrib import admin
from . import models

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username','email','first_name','last_name','is_staff','about']
    list_per_page = 15
    search_fields = ['username__istartswith']

@admin.register(models.Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['post','author','content','published_date','status']
    list_per_page = 15
    

@admin.register(models.Post)
class PostsAdmin(admin.ModelAdmin):
    list_display=['title','content','author','publish_date','status','slug']
    list_per_page = 15
    search_fields = ['title__istartswith']
    
    


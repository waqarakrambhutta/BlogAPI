from rest_framework import serializers
from .models import Author,Post,Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','username','email','first_name','last_name','is_staff','about']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','content','author','publish_date','status','slug']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','Heading','post','author','content','published_date','status']
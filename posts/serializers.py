from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        auther_id = self.context['author_id']
        return Author.objects.create(auther_id=auther_id,**validated_data)

    def save(self, **kwargs):
        return super().save(**kwargs)
            

    class Meta:
        model = Author
        fields = ['id','username','email','first_name','last_name','is_staff','about']
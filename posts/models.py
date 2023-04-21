from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField()
    about = models.TextField()

    def __str__(self) -> str:
        return self.username

class Post(models.Model):
    POST_STATUS_DRAFT='d'
    POST_STATUS_PUBLISHED= 'P'
    POST_STATUS_DELETED = 'D'
    POST_STATUS_CHOICES = [
        (POST_STATUS_DRAFT,'draft'),
        (POST_STATUS_PUBLISHED,'published'),
        (POST_STATUS_DELETED,'deleted')
    ]
    title = models.CharField(max_length=255)
    content =  models.TextField()
    author = models.ForeignKey(Author,on_delete=models.PROTECT,related_name='Author')
    publish_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
                        max_length=1,
                        choices=POST_STATUS_CHOICES,
                        default=POST_STATUS_DRAFT)
    slug = models.SlugField(unique=True,max_length=255)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    COMMENT_STATUS_APPROVED = 'A'
    COMMENT_STATUS_PENDING = 'P'
    COMMENT_STATUS_SPAM = 'S'

    COMMENT_STATUS = [
        (COMMENT_STATUS_APPROVED,'approved'),
        (COMMENT_STATUS_PENDING,'pending'),
        (COMMENT_STATUS_SPAM,'spam')
    ]
    Heading = models.CharField(max_length=50)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author_comments')
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1,choices=COMMENT_STATUS,default=COMMENT_STATUS_PENDING)
    
    def __str__(self) -> str:
        return self.Heading

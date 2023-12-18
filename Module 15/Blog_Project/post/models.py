from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # 1 post can in multipe post and 1 category can have multiple post
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
    
    
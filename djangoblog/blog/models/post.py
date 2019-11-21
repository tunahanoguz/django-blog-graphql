from django.db import models
from .category import Category
import datetime

class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(default = datetime.datetime.now)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
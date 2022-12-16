from django.db import models
import datetime
class ArticlesModel(models.Model):
    title =models.CharField(max_length=50)
    URL = models.URLField( )
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
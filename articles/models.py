from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    owner = models.ForeignKey(User , related_name='article_owner' , on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    date = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    save_for_you = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date']

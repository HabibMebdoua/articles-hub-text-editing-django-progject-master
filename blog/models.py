from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    subject = RichTextField()
    date = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return self.title

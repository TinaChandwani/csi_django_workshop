from django.db import models
from datetime import datetime
# Create your models here.
class Arts(models.Model):
    title = models.CharField(max_length=100)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    author = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_at = models.DateTimeField(default = datetime.now , blank = True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Arts"
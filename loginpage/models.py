from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    text = models.TextField()

    def __str__(self):
        return self.title

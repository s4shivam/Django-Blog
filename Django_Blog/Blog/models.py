from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        if(len(self.content)>160):
            return self.content[:160]
        else:
            return self.content
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

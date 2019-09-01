from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Sys_user(models.Model):
    user = models.OneToOneField( User , on_delete='CASCADE')
    def __str__(self):
        return str(self.user.username)

class Article(models.Model):
    publisher = models.ForeignKey(Sys_user , related_name='articels',on_delete = 'CASCADE')
    title = models.CharField(max_length = 50)
    article = models.TextField()

    def __str__(self):
        return str(self.title)



    def get_absolute_url(self):
        return reverse("Art:ArticleList")

class Comment(models.Model):
    art = models.ForeignKey(Article , related_name='com' ,on_delete='CASCADE')
    comment = models.TextField()

    def __str__(self):
        return self.comment
        
    def get_absolute_url(self):
        return reverse("Art:ArticleList" , kwargs={'pk':self.pk})

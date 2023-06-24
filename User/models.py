from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    age  = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=256, default="No Title")
    content = models.TextField(default="")
    author = models.ForeignKey('User', on_delete=models.CASCADE)

class Comments(models.Model):
    comment = models.TextField(default="")
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
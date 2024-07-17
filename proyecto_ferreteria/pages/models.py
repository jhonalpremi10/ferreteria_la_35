# pages/models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    # Tu modelo de Blog aquí

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)





from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=10)

    def __str__(self):
        return self.category_name
    


class Tasty(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='tasty/%Y/%m/%d')
    text = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name






class TastyComment(models.Model):
    '''
    댓글 모델
    '''
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    tasty = models.ForeignKey(Tasty, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    score = models.PositiveIntegerField()

    def __str__(self):
        return self.writer.username+' / '+self.comment_text


class TastyScore(models.Model):
    pass
    
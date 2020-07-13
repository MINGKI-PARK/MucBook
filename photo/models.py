from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_images.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + ' / ' + self.created.strftime('%Y-%m-%d %H:%M:%S')

    
    # def get_absolute_url(self):
    #     return reverse('photo:photo_detail', args=[str(self.id)])


class Comment(models.Model):
    '''
    댓글 모델
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.author.username+' / '+self.comment_text
    
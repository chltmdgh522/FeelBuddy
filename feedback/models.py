from django.db import models

from users.models import User


class Community(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    img_url = models.ImageField(upload_to='images/', blank=True, null=True)  #TextField를 ImageField로 변경
    create_community = models.DateField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    content = models.TextField()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    create_like = models.DateField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
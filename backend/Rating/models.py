from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile')
    avatar = models.ImageField(upload_to='avatar_image', blank=True, null=True)
    rank = models.IntegerField(default=0)
    warn = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Post')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='skatepark_image', blank=True, null=True)
    rating = models.ForeignKey('Rating', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


RATING = (
    (1, "1.0"),
    (2, "2.0"),
    (3, "3.0"),
    (4, "4.0"),
    (5, "5.0"),
)


class Rating(models.Model):
    rating = models.IntegerField(choices=RATING)

from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=150)
    post_body = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)
    published_on = models.DateTimeField(auto_now_add=True)
class Meta:
    def __str__(self):
        return self.title()
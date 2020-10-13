from django.db import models
STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published'),

)
class Post(models.Model):
    title = models.CharField(max_length=150)
    post_body = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)
    published_on = models.DateTimeField(auto_now_add=True)
    status_choices = models.CharField(max_length=10, choices=STATUS, default='draft')
class Meta:
    ordering = ('published_on',)
    def __str__(self):
        return self.title()
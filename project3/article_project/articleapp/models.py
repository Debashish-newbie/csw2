from django.db import models
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Article.Status.PUBLISHED)
    
class Article(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    objects = models.Manager()
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    status = models.CharField(
    max_length=2,
    choices=Status.choices,
    default=Status.DRAFT
)
    published = PublishedManager()
    publish=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

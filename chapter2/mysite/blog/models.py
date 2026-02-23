
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    body = models.TextField()
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT)
    
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)#store the date and time when the post is first created
    updated=models.DateTimeField(auto_now=True) #store the date and time when the post is last updated
    
    class Meta:
        ordering = ('-publish',) #order the posts by publish date in descending order
        # - means descending order, + means ascending order
        indexes = [models.Index(fields=['-publish'])] #create an index on the publish field in descending order    
    def __str__(self):
        return self.title

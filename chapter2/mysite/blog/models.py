
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
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

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish') #slug is a short label for something, containing only letters, numbers, underscores or hyphens. unique_for_date means that the slug must be unique for the given date.
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
    tags = TaggableManager()
    
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)#store the date and time when the post is first created
    updated=models.DateTimeField(auto_now=True) #store the date and time when the post is last updated
    
    class Meta:
        ordering = ('-publish',) #order the posts by publish date in descending order
        # - means descending order, + means ascending order
        indexes = [models.Index(fields=['-publish'])] #create an index on the publish field in descending order    
    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse(
    #         'blog:post_detail', 
    #         args=[self.id]
    #         )
    def get_absolute_url(self):
        return reverse(
            'blog:post_slug_date_detail', 
            args=[self.publish.year, 
                  self.publish.month, 
                  self.publish.day, 
                  self.slug
                ]    
            )
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    name = models.CharField(max_length=80)
    email = models.EmailField()

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
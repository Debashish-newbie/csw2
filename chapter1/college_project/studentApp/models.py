
from django.db import models
from django.utils import timezone
from django.conf import settings


class student(models.Model):
    name= models.CharField(max_length=100)
    age = models.IntegerField()
    roll_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    dept = models.CharField(
        max_length=100,
        default='CSE',
        )
    
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        ordering = ('-age',) 
        indexes = [models.Index(fields=['-age'])]  
    def __str__(self):
        return self.name   
from django.db import models

# Create your models here.

        
class Book(models.Model):
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    author = models.CharField(max_length=254, blank=False)
    ISBN = models.TextField(blank=False)
    date = models.DateField(null=False)
    
    def __str__(self):
        return self.name
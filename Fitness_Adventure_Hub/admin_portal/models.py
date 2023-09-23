from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='activity_images/')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    interest = models.TextField()

    def __str__(self):
        return self.name
    
class Configuration(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.key
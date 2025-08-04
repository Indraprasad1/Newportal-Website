from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Category'
    
    def __str__(self):
        return self.title
    
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=80)
    sub_title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="imgs/", max_length=250, null=True, default=None)
    details=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)  # Add this field to track views
    
    class Meta:
        verbose_name_plural='News'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    comments=models.TextField()
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Articles(models.Model):
    title = models.CharField(max_length=100)
    sub_title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="imgs/", max_length=250, null=True, default=None)
    details=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)  # Add this line
    
    class Meta:
        verbose_name_plural='Articles'
    
    def __str__(self):
        return self.title
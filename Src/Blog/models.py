from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural='Category'
        
    def __str__(self):
        return self.name


class Blog(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=80)
    sub_title=models.CharField(max_length=100)
    details=models.TextField()
    image=models.ImageField(upload_to="image/", max_length=250, null=True, default=None)
    date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Blog'
    
    def __str__(self):
        return self.title



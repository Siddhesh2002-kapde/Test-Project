from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    Cat_image = models.ImageField(upload_to='Cat_image/',default=True)

    def __str__(self):
        return self.category
    
    
class Blog(models.Model):
    category = models.ForeignKey(Category, default=True, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/',default=True)

    def __str__(self):
        return self.title
    




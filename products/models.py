from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to="uploads/CategoryImage/", blank=True, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=155)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/porductImage/", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
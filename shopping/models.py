from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.FloatField()
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return self.title

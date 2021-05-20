from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank='true')
    description = models.TextField()
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    product_image = models.ImageField(null=True,blank=True,upload_to="images/")
   
    def __str__(self) :
        return self.name
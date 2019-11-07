from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    """ No default product will be added int the database """
    description = models.TextField()
    """ A description of what the product is """
    price = models.DecimalField(max_digits=6, decimal_places=2)
    """ Pricing model will be less than £1m and decimal places = pence """
    image = models.ImageField(upload_to='images')
    """ Allow images to be uploaded for our products """
    
    def __str__(self):
        return self.name  # A string will be returned with the name
        
        
        
    

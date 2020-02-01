from django.db import models

class Predictor(models.Model):
    city= models.TextField(null='True')
    country= models.TextField()
    temperature = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    
    def __str__(self):
        return self.city




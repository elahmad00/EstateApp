from django.db import models

class Listing(models.Model):
    realtor = models.EmailField(max_length=255)
    

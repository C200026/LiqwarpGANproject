from django.db import models
from datetime import date

class ModelFile(models.Model):
    image = models.ImageField(upload_to='documents/')
    
    #uploaded_at = models.DateTimeField(auto_now_add=True)
    #output = models.ImageField(default = 'output/output.jpg')

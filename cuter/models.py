from django.db import models

# Create your models here.

class Address(models.Model):
    url = models.CharField(max_length=256, default=None)
    shortcut = models.CharField(max_length=40)


    class Meta:
        db_table = 'addresses'
        verbose_name_plural = "addresses"
        
    
    def __str__(self):
        return str(self.shortcut)
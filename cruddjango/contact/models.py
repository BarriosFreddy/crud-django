from django.db import models

# Create your models here.
class Contact(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)
    elastname = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    ephonenumber = models.CharField(max_length=15)  
    class Meta:  
        db_table = "contact"  

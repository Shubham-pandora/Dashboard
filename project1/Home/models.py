from django.db import models

# Create your models here.

class WebBeta1(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)
    ip2 = models.CharField(max_length=200,blank=True)
    ip3 = models.CharField(max_length=200,blank=True)
    ip4 = models.CharField(max_length=200,blank=True)
    ip5 = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.service_name
        
class WebBeta2(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)
    ip2 = models.CharField(max_length=200,blank=True)
    ip3 = models.CharField(max_length=200,blank=True)
    ip4 = models.CharField(max_length=200,blank=True)
    ip5 = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.service_name    
    
class WebBeta3(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)
    ip2 = models.CharField(max_length=200,blank=True)
    ip3 = models.CharField(max_length=200,blank=True)
    ip4 = models.CharField(max_length=200,blank=True)
    ip5 = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.service_name
    
class WebBeta4(models.Model):
    service_name = models.CharField(max_length=200)
    ip1 = models.CharField(max_length=200,blank=True)
    ip2 = models.CharField(max_length=200,blank=True)
    ip3 = models.CharField(max_length=200,blank=True)
    ip4 = models.CharField(max_length=200,blank=True)
    ip5 = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.service_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)   
    # date = models.DateField()

    def __str__(self):
        return self.name



    


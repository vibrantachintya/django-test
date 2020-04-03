from django.db import models

# Create your models here.

class Person(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth = models.DateField()

class Car(models.Model):

    id =  models.AutoField(primary_key = True)
    mode = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return "Model is %s, %i price : %i" % (self.mode, self.price, self.id)

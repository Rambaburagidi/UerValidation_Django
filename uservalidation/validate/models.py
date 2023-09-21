from django.db import models

# Create your models here.
class validate(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    mail=models.EmailField()
    qualification=models.CharField(max_length=100)
    percentage=models.IntegerField()
    place=models.CharField(max_length=100)
    phone=models.BigIntegerField()
class Meta:
    db_table="validate"
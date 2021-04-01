from django.db import models

# Create your models here.

class Enterprise(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Nit = models.BigIntegerField(null=True, unique=True)
    Gln = models.BigIntegerField()

class Code(models.Model):
    Id = models.IntegerField(primary_key=True)
    Owner = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100, null=True)    
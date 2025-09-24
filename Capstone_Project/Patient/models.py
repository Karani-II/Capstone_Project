from django.db import models
from django.contrib.auth.models import User 
class Patient_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Date_of_birth = models.DateField()
    weight = models.FloatField() 
    height = models.FloatField()
    BP_diastolic = models.IntegerField()
    Bp_systolic = models.IntegerField()
    Allergies = models.TextField(blank = True, null= True)

# Create your models here.

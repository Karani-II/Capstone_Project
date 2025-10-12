from django.db import models
from django.contrib.auth.models import User 

class Pharmacist_Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    Registration_No = models.CharField()
    contact = models.IntegerField()
class prescription(models.Model)

# Create your models here.

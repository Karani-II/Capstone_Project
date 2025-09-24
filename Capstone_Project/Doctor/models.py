from django.db import models
from django.contrib.auth.models import User 
from Patient.models import Patient_Profile 
class Doctor_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Speciality = models.CharField(max_length = 200)
    availabiity_schedule = models.TextField(blank = True, null = True)
class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor_Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient_Profile, on_delete=models.CASCADE)
    day = models.DateField()    
    time = models.TimeField()
class Drugs(models.Model):
    generic_name = models.TextField(max_length = 200)
    strength = models.CharField(max_length = 100)
    dosage_form = models.CharField(max_length = 100)
class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor_Profile, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient_Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('amended', 'Amended'),
        ('dispensed', 'Dispensed'),
        ('cancelled', 'Cancelled'),
    ], default='active')
class Prescription_Item(models.Model):
    prescription = models.ForeignKey(Prescription,related_name='items' ,on_delete=models.CASCADE)
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    dosage = models.CharField(max_length = 100)
    frequency = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 100)
    instructions = models.TextField()
class PatientNotes():
    patient = models.ForeignKey (Patient_Profile, on_delete = models.CASCADE)
    Doctor = models.ForeignKey(Doctor_Profile, on_delete=models.CASCADE)
    patient_History = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)



# Create your models here.

from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from Patient.models import Patient_Profile 
from django.apps import apps


class Pharmacist_Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    Registration_No = models.CharField()
    contact = models.IntegerField()

class prescription_handling(models.Model):
    ACTION_CHOICES = [
        ('added', 'Added Item'),
        ('amended', 'Amended Item'),
        ('deleted', 'Deleted Item'),
        ('dispensed', 'Dispensed Prescription'),
    ]
    prescription = models.ForeignKey('Doctor.Prescription' ,on_delete = models.CASCADE)
    pharmacist = models.ForeignKey(Pharmacist_Profile , on_delete = models.CASCADE)
    item = models.ForeignKey('Doctor.Prescription_Item' ,on_delete = models.SET_NULL, null = True, blank = True)
    action = models.CharField(max_length = 20 , choices = ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add = True)
    notes = models.TextField(blank = True )
class InventoryItem(models.Model):
    pharmacist = models.ForeignKey(Pharmacist_Profile, on_delete=models.CASCADE, related_name='inventory')
    drug = models.ForeignKey('Pharmacist.Drugs', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_restocked = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def restock(self, amount):
        self.quantity += amount
        self.last_restocked = timezone.now()
        self.save()

    def dispense(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            self.save()
        else:
            raise ValueError("Not enough stock available.")
        
class Drugs(models.Model):
    generic_name = models.TextField()
    strength = models.CharField(max_length = 100)
    dosage_form = models.CharField(max_length = 100)

class DrugBatch(models.Model):
    drug = models.ForeignKey(Drugs , on_delete = models.CASCADE, related_name = 'batches' )
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='batches')
    batch_number = models.CharField(max_length=100)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    quantity_received  = models.PositiveIntegerField()
    quantity_remaining = models.PositiveIntegerField()
    supplier = models.CharField(max_length=200, blank=True, null=True)
    received_by = models.ForeignKey(Pharmacist_Profile, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Refill_appointment(models.Model):
    drug_refill = models.ForeignKey(Drugs , on_delete=models.SET_NULL, null=True, blank=True)
    dosage = models.CharField(default = "null")
    frequency = models.CharField(default = "null")
    duration = models.CharField(default = "null")
    refilling_patient = models.ForeignKey(Patient_Profile, on_delete=models.SET_NULL, null=True , blank=True )
    refilling_date = models.DateTimeField()





    



# Create your models here.

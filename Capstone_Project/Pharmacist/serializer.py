from rest_framework import serializers 
from .models import Pharmacist_Profile ,prescription_handling, InventoryItem, Drugs, DrugBatch, Refill_appointment

class Pharmacist_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist_Profile 
        fields = '__all__'

class prescription_handlingSerializer(serializers.ModelSerializer):
    class Meta:
        model = prescription_handling 
        fields = '__all__'
class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs 
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    drug = DrugsSerializer(read_only=True)
    drug_id = serializers.PrimaryKeyRelatedField(
        queryset=Drugs.objects.all(), source='drug', write_only=True
    )
    class Meta:
        model = InventoryItem
        fields = ['id', 'pharmacist', 'drug', 'drug_id', 'quantity', 'unit_price', 'last_restocked', 'expiry_date']

class DrugBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugBatch 
        fields = '__all__'

class Refill_appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refill_appointment 
        fields = '__all__'
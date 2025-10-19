from rest_framework import serializers 
from rest_framework import views 
from .models import Doctor_Profile, Appointments , Prescription ,Prescription_Item , PatientNotes 

class Doctor_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Profile 
        fields = '__all__'

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments 
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class Prescription_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription_Item 
        fields = '__all__'

class PatientNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientNotes
        fields = '__all__'

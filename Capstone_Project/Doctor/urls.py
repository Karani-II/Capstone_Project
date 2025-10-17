from rest_framework.routers import DefaultRouter
from .views import (
    Doctor_Profileviews,
    Appointmentsviews,
    Prescriptionviews,
    Prescription_Itemviews,
    PatientNotesviews
)

router = DefaultRouter()
router.register(r'doctors', Doctor_Profileviews)
router.register(r'appointments', Appointmentsviews)
router.register(r'prescriptions', Prescriptionviews)
router.register(r'prescription-items', Prescription_Itemviews)
router.register(r'patient-notes', PatientNotesviews)

urlpatterns = router.urls

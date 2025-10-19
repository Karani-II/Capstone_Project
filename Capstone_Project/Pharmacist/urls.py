from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    Pharmacist_Profileview, Drugsview, InventoryItemview,
    DrugBatchview, prescription_handlingview, Refill_appointmentview,
)

router = DefaultRouter()
router.register(r'pharmacists', Pharmacist_Profileview)
router.register(r'drugs', Drugsview)
router.register(r'inventory', InventoryItemview)
router.register(r'batches', DrugBatchview)
router.register(r'prescription-handling', prescription_handlingview)
router.register(r'refill-appointments', Refill_appointmentview)

urlpatterns = router.urls


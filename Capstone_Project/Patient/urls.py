from rest_framework.routers import DefaultRouter 
from .models import Patient_Profile 

router = DefaultRouter()
router.register(r'Patient' , Patient_Profile)

urlpatterns = router.urls 
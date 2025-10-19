from rest_framework.routers import DefaultRouter 
from .views import Patient_Profileview

router = DefaultRouter()
router.register(r'Patient' , Patient_Profileview)

urlpatterns = router.urls 
from .views import CandidateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/v1/ats/candidate', CandidateViewSet, basename='candidate')
urlpatterns = router.urls

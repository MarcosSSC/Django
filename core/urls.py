from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('department', viewsets.DepartmentViewSet)
router.register('zone', viewsets.ZoneViewSet)

urlpatterns = router.urls

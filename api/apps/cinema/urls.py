from rest_framework import routers
from .views import CinemaViewSet, HallViewSet, EventViewSet

router = routers.DefaultRouter()

router.register('cinema', CinemaViewSet, basename='cinema')
router.register('hall', HallViewSet, basename='hall')
router.register('event', EventViewSet, basename='event')


urlpatterns = router.urls

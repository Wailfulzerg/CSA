from rest_framework import routers
from .views import CustomUserViewSet

router = routers.DefaultRouter()

router.register('users', CustomUserViewSet,  basename='users')

urlpatterns = router.urls

from django.contrib import admin
from .models import NotificationViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('event', NotificationViewSet, base_name='models')

urlpatterns = router.urls
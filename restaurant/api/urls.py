from django.urls import path, include
from rest_framework import routers

from .views import FoodViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('foods', FoodViewSet)

urlpatterns = [
    path('', include(router.urls))
]

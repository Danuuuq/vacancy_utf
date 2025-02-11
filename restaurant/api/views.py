from rest_framework import viewsets

from dishes.models import FoodCategory
from .serializers import FoodListSerializer


class FoodViewSet(viewsets.ModelViewSet):
    model = FoodCategory
    queryset = FoodCategory.objects.with_related_data()
    serializer_class = FoodListSerializer
    http_method_names = ['get']

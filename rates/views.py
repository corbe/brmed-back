# -*- coding: utf-8 -*-
from rest_framework import generics
from .models import Rate
from .serializers import RateSerializer
from .paginations import CustomPagination

class RateList(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = CustomPagination

    def get_object(self):
        return get_object_or_404(Rate, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return Rate.objects.filter().order_by('-date')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

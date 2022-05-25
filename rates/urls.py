from django.urls import path

from . import views

urlpatterns = [
    path('', views.RateList.as_view(), name='rates'),
]

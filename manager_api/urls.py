from django.urls import include, path
from rest_framework import routers

from .views import SampleViewSet


router = routers.DefaultRouter()
router.register(r'sample', SampleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]


# path('api-auth/', include('rest_framework.urls'))

from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('sneakers', views.SneakerViewSet, basename="sneakers")
router.register('sizes', views.SizeViewSet, basename="sizes")
router.register('sneakers-elasticsearch', views.SneakerDocumentViewSet, basename="sneakers-elasticsearch")

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, FloorViewSet, RoomViewSet, RoomTypeViewSet, TaskViewSet, MaintenanceRequestViewSet, \
    TeamViewSet, StatusViewSet, EquipmentTypeViewSet, EquipmentViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'floors', FloorViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'room-types', RoomTypeViewSet)
router.register(r'status', StatusViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'maintenance-requests', MaintenanceRequestViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'equipment-types', EquipmentTypeViewSet)
router.register(r'equipments', EquipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
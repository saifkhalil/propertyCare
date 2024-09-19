from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, FloorViewSet, RoomViewSet, RoomTypeViewSet, TaskViewSet, MaintenanceRequestViewSet, \
    TeamViewSet, StatusViewSet, EquipmentTypeViewSet, EquipmentViewSet, IssueViewSet, IssueTypeViewSet, \
    filter_issue_types

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
router.register(r'issue-types', IssueTypeViewSet)
router.register(r'issues', IssueViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('filter_issue_types/', filter_issue_types, name='filter_issue_types'),
]
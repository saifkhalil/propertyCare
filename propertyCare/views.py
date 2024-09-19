from rest_framework import viewsets
from django.http import JsonResponse
from .models import Property, Floor, Room, RoomType, Task, MaintenanceRequest, Status, Team, EquipmentType, Equipment, \
    Issue, IssueType
from .serializers import PropertySerializer, FloorSerializer, RoomSerializer, RoomTypeSerializer, TaskSerializer, \
    MaintenanceRequestSerializer, StatusSerializer, TeamSerializer, EquipmentTypeSerializer, EquipmentSerializer, \
    IssueTypeSerializer, IssueSerializer


class BaseViewSet(viewsets.ModelViewSet):
    """
    Base viewset to handle common logic for perform_create and perform_update.
    """

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, created_at=timezone.now())

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user, modified_at=timezone.now())


class PropertyViewSet(BaseViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class FloorViewSet(BaseViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer


class RoomViewSet(BaseViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomTypeViewSet(BaseViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class StatusViewSet(BaseViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TaskViewSet(BaseViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TeamViewSet(BaseViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MaintenanceRequestViewSet(BaseViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

class EquipmentViewSet(BaseViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class EquipmentTypeViewSet(BaseViewSet):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer

class IssueTypeViewSet(BaseViewSet):
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer


class IssueViewSet(BaseViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

def filter_issue_types(request):
    equipment_id = request.GET.get('equipment_id')
    issue_types = IssueType.objects.filter(equipment_id=equipment_id).values('id', 'type')
    return JsonResponse({'issue_types': list(issue_types)})
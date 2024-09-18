from rest_framework import serializers
from .models import Property, Floor, Room, RoomType, Team, MaintenanceRequest, Task, Status, EquipmentType, Equipment


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(read_only=True)
    room_type_id = serializers.PrimaryKeyRelatedField(queryset=RoomType.objects.all(), write_only=True, source='room_type')

    class Meta:
        model = Room
        fields = ['id', 'name', 'size', 'room_type', 'room_type_id', 'created_at', 'created_by', 'modified_at', 'modified_by']


class FloorSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Floor
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    floors = FloorSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    type = EquipmentTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(queryset=EquipmentType.objects.all(), write_only=True, source='type')

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'type', 'type_id', 'assigned_team', 'auto_assigned_team']


class MaintenanceRequestSerializer(serializers.ModelSerializer):
    equipments = EquipmentSerializer(many=True, read_only=True)
    equipment_ids = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(), write_only=True, many=True,
                                                       source='equipments')

    class Meta:
        model = MaintenanceRequest
        fields = ['id', 'property', 'issue_description', 'request_date', 'status', 'assigned_team', 'equipments',
                  'equipment_ids']

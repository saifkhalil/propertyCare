from django.contrib import admin
from .models import Property, Floor, Room, RoomType, Task, MaintenanceRequest, Team, EquipmentType, Equipment, Status


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'created_by', 'modified_at', 'modified_by']
    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)  # Pass request.user to the model's save method

@admin.register(Property)
class PropertyAdmin(BaseAdmin):
    list_display = ('name', 'location', 'size', 'owner', 'created_at', 'created_by', 'modified_at', 'modified_by')


@admin.register(Floor)
class FloorAdmin(BaseAdmin):
    list_display = ('name', 'property', 'number_of_rooms', 'created_at', 'created_by', 'modified_at', 'modified_by')


@admin.register(Room)
class RoomAdmin(BaseAdmin):
    list_display = ('name', 'floor', 'room_type', 'size', 'created_at', 'created_by', 'modified_at', 'modified_by')


@admin.register(RoomType)
class RoomTypeAdmin(BaseAdmin):
    list_display = ('type_name', 'created_at', 'created_by', 'modified_at', 'modified_by')


@admin.register(Task)
class TaskAdmin(BaseAdmin):
    list_display = ('title', 'description', 'assigned_to', 'assigned_team', 'due_date', 'status', 'created_at', 'created_by', 'modified_at', 'modified_by')

@admin.register(Status)
class StatusAdmin(BaseAdmin):
    list_display = ('name', )


@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(BaseAdmin):
    list_display = ('property', 'floor', 'room', 'issue_description', 'request_date', 'status', 'created_at', 'created_by', 'modified_at', 'modified_by')


@admin.register(Team)
class TeamAdmin(BaseAdmin):
    list_display = ('name', 'created_at', 'created_by', 'modified_at', 'modified_by')
    filter_horizontal = ('members',)

@admin.register(EquipmentType)
class EquipmentTypeAdmin(BaseAdmin):
    list_display = ('name', 'created_at', 'created_by', 'modified_at', 'modified_by')

@admin.register(Equipment)
class EquipmentAdmin(BaseAdmin):
    list_display = ('name', 'type', 'assigned_team', 'auto_assigned_team', 'created_at', 'created_by', 'modified_at', 'modified_by')
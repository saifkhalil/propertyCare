from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="%(class)s_created_by", on_delete=models.SET_NULL, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, related_name="%(class)s_modified_by", on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)

        if not self.pk:
            self.created_at = timezone.now()
            if user:
                self.created_by = user
        else:
            self.modified_at = timezone.now()
            if user:
                self.modified_by = user

        super(BaseModel, self).save(*args, **kwargs)




class Property(BaseModel):
    name = models.CharField(max_length=255)
    location = models.TextField()
    size = models.FloatField()
    owner = models.ForeignKey(User, related_name="properties", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Floor(BaseModel):
    property = models.ForeignKey(Property, related_name="floors", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number_of_rooms = models.IntegerField()

    def __str__(self):
        return self.name


class RoomType(BaseModel):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name


class Room(BaseModel):
    floor = models.ForeignKey(Floor, related_name="rooms", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete=models.CASCADE)
    size = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.room_type.type_name})"


class Status(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Team(BaseModel):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="teams")

    def __str__(self):
        return self.name

class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, related_name="tasks", on_delete=models.SET_NULL, null=True)
    assigned_team = models.ForeignKey(Team, related_name="task", on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField()
    status = models.ForeignKey(Status, related_name="%(class)s_status", on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class EquipmentType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Equipment(BaseModel):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(EquipmentType, related_name="equipment", on_delete=models.SET_NULL, null=True)
    assigned_team = models.ForeignKey(Team, related_name="equipment", on_delete=models.SET_NULL, null=True, blank=True)
    auto_assigned_team = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.type.name})"

class IssueType(BaseModel):
    equipment = models.ForeignKey(Equipment, related_name="issue_types", on_delete=models.CASCADE)
    type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type} ({self.equipment.name})"

class Issue(BaseModel):
    equipment = models.ForeignKey(Equipment, related_name="issues", on_delete=models.CASCADE)
    issue_type = models.ForeignKey(IssueType, related_name="issues", on_delete=models.SET_NULL, null=True, blank=True)
    note = models.TextField()

    def __str__(self):
        return f"Issue with {self.equipment.name} - {self.issue_type.type}"

class MaintenanceRequest(BaseModel):
    property = models.ForeignKey(Property, related_name="maintenance_requests", on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, related_name="maintenance_request", on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, related_name="maintenance_request", on_delete=models.CASCADE, null=True)
    issues = models.ManyToManyField(Issue, related_name="maintenance_requests")
    issue_description = models.TextField()
    request_date = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, related_name="%(class)s_status", on_delete=models.CASCADE)
    # assigned_team = models.ForeignKey(Team, related_name="maintenance_request", on_delete=models.SET_NULL, null=True)
    equipments = models.ManyToManyField(Equipment, related_name="maintenance_request")

    def __str__(self):
        return f"{self.property.name} - {self.status}"


@receiver(m2m_changed, sender=MaintenanceRequest.equipments.through)
def create_tasks_for_equipment(sender, instance, action, **kwargs):
    """
    This signal is triggered when the m2m relationship for 'equipments' changes.
    It creates tasks for equipment with auto_assigned_team set to True.
    """
    # 'post_add' ensures this is triggered after the equipment is added
    if action == "post_add":
        for equipment in instance.equipments.all():
            if equipment.auto_assigned_team and equipment.assigned_team:
                Task.objects.create(
                    title=f"Maintenance for {equipment.name}",
                    description=f"Maintenance request for {instance.property.name} regarding {equipment.name}",
                    assigned_to=None,  # Assigned to the team
                    assigned_team=equipment.assigned_team,
                    due_date=instance.request_date,
                    status=Status.objects.get(id=1),
                    created_by=instance.created_by,  # Set to the creator of the maintenance request
                    modified_by=instance.created_by  # Initially set to the creator
                )
# Property Care Management System

A Django-based property care management system for managing properties, floors, rooms, tasks, maintenance requests, equipment, and auto-assigned teams.

## Features

- Manage properties, floors, rooms, and equipment.
- Assign maintenance tasks to teams based on equipment configurations.
- Auto-create tasks for equipment with auto-assigned teams.
- Track maintenance requests, equipment, and task statuses.
- Full CRUD API powered by Django REST Framework (DRF).
- Admin interface for easy management of all entities.
- Tracks `created_at`, `modified_at`, `created_by`, and `modified_by` for audit purposes.

## Models

### Property
- **name**: The name of the property.
- **location**: The location of the property.
- **size**: The size of the property.
- **owner**: The owner of the property.

### Floor
- **property**: The related property.
- **name**: The name of the floor.
- **number_of_rooms**: The number of rooms on the floor.

### Room
- **floor**: The related floor.
- **name**: The name of the room.
- **room_type**: The type of room (e.g., Bedroom, Living Room).
- **size**: The size of the room.

### Equipment
- **name**: The name of the equipment (e.g., Air Conditioner).
- **type**: The type of equipment (related to the `EquipmentType` model).
- **assigned_team**: The team responsible for the equipment.
- **auto_assigned_team**: Boolean flag to auto-create tasks for the assigned team when a maintenance request is created.

### EquipmentType
- **name**: The type of equipment (e.g., Cooling System, Heating System).

### MaintenanceRequest
- **property**: The related property.
- **issue_description**: Description of the maintenance issue.
- **request_date**: The date the maintenance request was created.
- **status**: The current status of the request (Open, In Progress, Resolved, Closed).
- **assigned_team**: The team assigned to handle the maintenance request.
- **equipments**: A list of equipment related to the maintenance request.

### Task
- **title**: The title of the task.
- **description**: A description of the task.
- **assigned_to**: The team responsible for the task.
- **due_date**: The due date of the task.
- **status**: The current status of the task (Pending, In Progress, Completed).

## Installation

### Prerequisites

- Python 3.x
- Django 3.x+
- Django REST Framework
- PostgreSQL (optional, but recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/saifkhalil/propertyCare.git
cd propertyCare
```
### Step 2: Set Up a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```
### Step 3: Install the Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Configure the Database
In the settings.py file, configure your database (e.g., PostgreSQL or SQLite):

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### Step 5: Apply Migrations
```bash
python manage.py migrate
```
### Step 6: Create a Superuser
````bash
python manage.py createsuperuser
````

### Step 7: Run the Development Server
```bash
python manage.py runserver
```

Visit ```http://localhost:8000/admin/ ```to access the Django admin interface.

### API Endpoints
The system includes a full API for managing properties, maintenance requests, tasks, and more.

Visit ```http://localhost:8000/api/swagger ```to access the Swagger Documentation.


#### Available Endpoints:
* ```/api/properties/``` (GET, POST)
* ```/api/floors/``` (GET, POST)
* ```/api/rooms/``` (GET, POST)
* ```/api/equipments/``` (GET, POST)
* ```/api/equipment-types/``` (GET, POST)
* ```/api/maintenance-requests/``` (GET, POST)
* ```/api/tasks/``` (GET, POST)

* etc...

#### Example: Create a Maintenance Request
```bash
curl -X POST http://localhost:8000/api/maintenance-requests/ \
-H "Content-Type: application/json" \
-d '{
  "property": 1,
  "issue_description": "Air conditioner not working",
  "request_date": "2024-09-15",
  "status": "open",
  "assigned_team": 2,
  "equipment_ids": [1, 2]
}'
```
## Custom Logic
### Auto-assigned Equipment Teams
When creating a ```MaintenanceRequest```, if any equipment has ```auto_assigned_team``` set to ```True```, a task will be automatically created and assigned to the team responsible for the equipment.


This logic is handled using Django signals to ensure the many-to-many relationship between ```MaintenanceRequest``` and ```Equipment``` is established before creating the tasks.

## Admin Interface
The project comes with an admin interface for managing:

* Properties
* Floors
* Rooms
* Equipment
* Equipment Types
* Maintenance Requests
* Tasks
* Teams
* etc...


# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contributions
Feel free to open issues or submit pull requests if you would like to contribute.

# Contact
For any questions or issues, contact saif.ibrahim@qi.iq.	
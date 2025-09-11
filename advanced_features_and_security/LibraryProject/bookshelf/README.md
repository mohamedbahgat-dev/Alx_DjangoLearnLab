# Django Custom Permissions & Groups Implementation

This document explains how custom permissions and user groups are configured in the Django application to enforce role-based access control (RBAC).
🧩 Key Features
• Custom Permissions: ⁠can_view, ⁠can_create, ⁠can_edit, ⁠can_delete for ⁠MyModel. • User Groups: ⁠Editors, ⁠Viewers, ⁠Admins with assigned permissions. • Secure Views: Permission checks in views using ⁠PermissionRequiredMixin.
🛠️ Configuration

1. Model Permissions
   Custom permissions are defined in the model's ⁠Meta class:

# myapp/models.py

from django.db import models

class MyModel(models.Model): # Fields...

    class Meta:
        permissions = [
            ("can_view", "Can view MyModel"),
            ("can_create", "Can create MyModel"),
            ("can_edit", "Can edit MyModel"),
            ("can_delete", "Can delete MyModel"),
        ]

Apply migrations to create permissions in the database:
python manage.py makemigrations
python manage.py migrate 2. Groups Setup
Groups are created programmatically or via the Django admin. Example code:

# myapp/management/commands/setup_groups.py

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from myapp.models import MyModel

def setup_groups():
content_type = ContentType.objects.get_for_model(MyModel)

    # Create groups
    editors, _ = Group.objects.get_or_create(name="Editors")
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions
    can_view = Permission.objects.get(codename="can_view", content_type=content_type)
    can_create = Permission.objects.get(codename="can_create", content_type=content_type)
    can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
    can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

    editors.permissions.set([can_edit, can_create])
    viewers.permissions.set([can_view])
    admins.permissions.set([can_view, can_create, can_edit, can_delete])

Run this script once to initialize groups. 3. Views with Permission Checks
Views use ⁠PermissionRequiredMixin to enforce access control:

# myapp/views.py

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

class MyModelCreateView(PermissionRequiredMixin, CreateView):
permission_required = 'myapp.can_create_mymodel'
model = MyModel
fields = '**all**'
template_name = 'myapp/mymodel_form.html'
success_url = reverse_lazy('mymodel-list')
Supported Views:
Action
View Class
Required Permission
Create
⁠CreateView
⁠can_create
Edit
⁠UpdateView
⁠can_edit
Delete
⁠DeleteView
⁠can_delete
View
⁠DetailView/⁠ListView
⁠can_view
🧪 Testing Permissions
Manual Testing 1. Create Test Users:
from django.contrib.auth.models import User, Group
user1 = User.objects.create_user('editor_user', password='password')
user1.groups.add(Group.objects.get(name='Editors')) 2. Test Scenarios:
▪ Log in as ⁠editor_user: Should allow create/edit, but not delete. ▪ Log in as ⁠viewer_user: Should only view data. ▪ Log in as ⁠admin_user: Should have full access. 3. Verify Template Logic:
In templates, use:
{% if user|has_perm:"myapp.can_edit_mymodel" %}
<a href="{% url 'edit' %}">Edit</a>
{% endif %}

Automated Testing
Example test case:

# myapp/tests.py

from django.test import TestCase, Client

class PermissionTests(TestCase):
def setUp(self):
self.client = Client()
self.editor = User.objects.create_user('editor', password='password')
self.editor.groups.add(Group.objects.get(name='Editors'))

    def test_editor_can_edit(self):
        self.client.login(username='editor', password='password')
        response = self.client.get('/edit/1/')
        self.assertEqual(response.status_code, 200)

🧭 Permissions Summary
Group
can_view
can_create
can_edit
can_delete
Viewers
✅
❌
❌
❌
Editors
✅
✅
✅
❌
Admins
✅
✅
✅
✅
🚨 Common Issues & Fixes
Issue
Solution
403 Forbidden errors
Ensure users are assigned to the correct group and permissions exist.
Missing permissions
Run ⁠makemigrations and ⁠migrate after adding permissions to models.
Template shows unauthorized actions
Verify permission checks use the correct codename (e.g., ⁠myapp.can_edit_mymodel).
📦 Usage Notes
• Replace ⁠myapp with your app's name in permission codenames. • Customize templates (⁠myapp/mymodel_form.html, etc.) to match your UI.
This setup ensures granular control over user actions and simplifies role-based access management. For more details, refer to the Django documentation on custom permissions.

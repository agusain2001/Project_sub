from django.db import models
from django.conf import settings

class Group(models.Model):
    name = models.CharField(max_length=255)
    group_type = models.CharField(max_length=50)  # e.g., hostel_roommates, project_teams, trip_groups
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_memberships')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
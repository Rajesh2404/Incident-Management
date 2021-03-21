from django.db import models
from django.contrib.auth.models import User

# Create your models here.

location_choices = (('Corporate Head office', 'Corporate Head office'),
                    ('Operations Department', 'Operations Department'),
                    ('Work Station', 'Work Station'),
                    ('Marketing Division', 'Marketing Division'),
                    )

severity_choices = (('Mild', 'Mild'),
                    ('Moderate', 'Moderate'),
                    ('Severe', 'Severe'),
                    ('Fatal', 'Fatal'),
                    )

sub_incident_choices = (('Environmental Incident', 'Environmental Incident'),
                    ('Injury/Illness', 'Injury/Illness'),
                    ('Property Damage', 'Property Damage'),
                    ('Vehicle', 'Vehicle'),
                    )


class Incidence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=50, choices=location_choices)
    department = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    incident_location = models.TextField()
    severity = models.CharField(max_length=50, choices=severity_choices)
    cause = models.TextField()
    action_taken = models.TextField()
    sub_incident = models.CharField(max_length=100, choices=sub_incident_choices)

    def __str__(self):
        return self.location

    class Meta:
        db_table = "incidentdb"
        ordering = ['date', 'time']
from django import forms
from Incident_app.models import Incidence


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class IncidentCreateForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ['location', 'department', 'date', 'time', 'incident_location', 'severity', 'cause', 'action_taken', 'sub_incident']

        widgets = {
            'department' : forms.Textarea(attrs={'class': 'form-style', 'rows': '3', 'autocomplete': 'off', 'required': '', 'placeholder': 'Department'}),
            'date' : DateInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': ''}),
            'time' : TimeInput(attrs={ 'class': 'form-style', 'autocomplete': 'off', 'required': ''}),
            'incident_location' : forms.TextInput(attrs={'class': 'form-style', 'autocomplete': 'off', 'required': '', 'placeholder': 'Incident Location'}),
            'cause' : forms.Textarea(attrs={'class': 'form-style', 'rows': '3', 'autocomplete': 'off', 'required': '', 'placeholder': 'Cause'}),
            'action_taken' : forms.Textarea(attrs={'class': 'form-style', 'rows': '3', 'autocomplete': 'off', 'required': '', 'placeholder': 'Action Taken'})
        }

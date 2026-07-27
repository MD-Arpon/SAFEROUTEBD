from django import forms
from .models import Incident, StreetLight, CrowdReport

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'category', 'severity', 'location_name', 'latitude', 'longitude', 'description', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief title of the incident'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Mugging, Harassment, Poor Lighting'}),
            'severity': forms.Select(attrs={'class': 'form-select'}),
            'location_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Dhanmondi Lake Road'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_latitude', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_longitude', 'step': 'any'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Provide details...'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class StreetLightForm(forms.ModelForm):
    class Meta:
        model = StreetLight
        fields = ['location_name', 'latitude', 'longitude', 'condition']
        widgets = {
            'location_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street or intersection name'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_latitude', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_longitude', 'step': 'any'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
        }


class CrowdReportForm(forms.ModelForm):
    class Meta:
        model = CrowdReport
        fields = ['location_name', 'latitude', 'longitude', 'density']
        widgets = {
            'location_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area name'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_latitude', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_longitude', 'step': 'any'}),
            'density': forms.Select(attrs={'class': 'form-select'}),
        }
from django import forms
from .models import Task

# Liaison des formulaires au modèle
class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['note', 'status']


class ConnexionForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

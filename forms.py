from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'description', 'is_active', 'start_date', 'end_date', 'response_count']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'toggle'}),
            'start_date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'response_count': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
        }


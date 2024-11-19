from django import forms
from .models import MoodEntry

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'note']
        widgets = {
            'mood': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'note': forms.Textarea(attrs={'rows': 3}),
        }

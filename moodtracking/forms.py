from django import forms
from .models import MoodLog

class MoodLogForm(forms.ModelForm):
    class Meta:
        model = MoodLog
        fields = ['mood_score', 'description']
        widgets = {
            'mood_score': forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '10'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
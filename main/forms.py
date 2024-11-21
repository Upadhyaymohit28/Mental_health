from django import forms
from moodtracking.models import MoodLog

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodLog
        fields = ['mood_score', 'sentiment_analysis_result']
        widgets = {
            'mood_score': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'sentiment_analysis_result': forms.Textarea(attrs={'rows': 3}),
        }

from django import forms
from .models import MoodLog

class MoodLogForm(forms.ModelForm):
    class Meta:
        model = MoodLog
        fields = ['mood_score', 'description']
        widgets = {
            'mood_score': forms.NumberInput(attrs={
                'type': 'range',  # Slider input type
                'min': '1',  # Minimum value
                'max': '10',  # Maximum value
                'step': '1',  # Step interval
                'style': 'width: 80%; appearance: none; height: 10px; background: linear-gradient(to right, #000000, #1e3a8a, #2563eb, #60a5fa, #e74c3c); border-radius: 5px; cursor: pointer; outline: none;',
                'value': '5',  
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Share what you are thinking here...',  # Placeholder text for the input box
                'style': 'width: 100%; height: 120px; border: 1px solid #ddd; border-radius: 8px; padding: 10px; font-size: 16px; resize: none; outline: none; background-color: #ffffff; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); color: #333;',
            }),
        }

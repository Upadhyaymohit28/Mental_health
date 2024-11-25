import json
from django import forms
from .models import UserProfile
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'preferences', 'mental_health_goals']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'preferences': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a word'}),
            'mental_health_goals': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your mental health goals'}),
        }

    def clean_preferences(self):
        preferences = self.cleaned_data.get('preferences', '').strip()
        if ' ' in preferences:  
            raise forms.ValidationError('Preferences should be a single word without spaces.')
        return preferences
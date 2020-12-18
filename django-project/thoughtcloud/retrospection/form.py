from django import forms 
from retrospection.models import Thought, Time

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['thought', 'done', 'date']




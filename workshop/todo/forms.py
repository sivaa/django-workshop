from django import forms
from todo.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Not enough words!")
        return name

from django import forms

class MovieForm(forms.Form):
    name = forms.CharField(required = True)

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Not enough words!")
        return name

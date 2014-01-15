from django import forms

from movies.models import Movie


class MovieForm(forms.ModelForm):
#    name = forms.CharField(required = True)

    class Meta:
        model = Movie

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Not enough words!")
        return name

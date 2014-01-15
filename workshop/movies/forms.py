from django import forms

class MovieForm(forms.Form):
    name = forms.CharField(required=False)

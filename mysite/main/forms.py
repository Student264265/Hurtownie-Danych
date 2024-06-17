from django import forms
from .models import HDData



class CreateNewData(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()
    k = forms.IntegerField()
    #shape = forms.ChoiceField(choices=HDData.Shape.choices)
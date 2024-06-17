from django import forms



class CreateNewData(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()
    k = forms.IntegerField()
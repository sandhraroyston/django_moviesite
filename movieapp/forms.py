from django import forms
from . models import Movielist

class Updatemovielist(forms.ModelForm):
    class Meta:
        model=Movielist
        fields=['name','desc','img','genre','year']


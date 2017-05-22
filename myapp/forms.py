from django import forms

class PlaceForm(forms.Form):
   placename = forms.CharField(max_length = 100)
   

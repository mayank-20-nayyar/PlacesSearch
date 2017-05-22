from django import forms

class PlaceForm(forms.Form):
   place = forms.CharField(max_length = 100)
   

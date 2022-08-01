from django import forms


class Contactus(forms.Form):

   text = forms.CharField(max_length=20, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'hello'}))












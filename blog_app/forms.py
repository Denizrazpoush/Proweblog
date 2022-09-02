from django import forms
from django.core.exceptions import ValidationError
from blog_app.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class Contactus(forms.Form):
   BIRTH_YEAR_CHOOSE = ['1999','1997','1993']


   text = forms.CharField(max_length=20, label='',
                    widget=forms.TextInput(attrs={'placeholder': 'your text'}))
   name = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'type your name'}))
   birth_year = forms.DateField(widget = forms.SelectDateWidget(years=BIRTH_YEAR_CHOOSE))

   def clean(self):

       text = self.cleaned_data.get('text')
       name = self.cleaned_data.get('name')

       if name == text:
           raise ValidationError("the text and the name are same ! ", code='name_text_same')

   def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'mother' or 'MOTHER' in name:
            raise ValidationError("you had mother in you name", code='213')
        return name
















from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:

            self.fields[field].widget.attrs.update({'class': 'form-control'})


class AddPropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        widgets = {'agent': forms.HiddenInput()}
        

    def __init__(self, *args, **kwargs):
        super(AddPropertyForm, self).__init__(*args, **kwargs)
        for field in self.fields:

            self.fields[field].widget.attrs.update({'class': 'form-control'})


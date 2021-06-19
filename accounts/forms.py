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

class RentTransactionForm(ModelForm):
    class Meta:
        model = RentTransaction
        fields = '__all__'
        widgets = {'owner': forms.HiddenInput(),'date':DateInput(),'agent': forms.HiddenInput(),'date': forms.HiddenInput()}
        

    def __init__(self,*args, **kwargs):
        super(RentTransactionForm, self).__init__(*args, **kwargs)        
        # self.request = kwargs.pop('request', None)
        # username = str(request.user)
        # agent = Agent.objects.get(username=username)
        # aid = agent.agent_id
        # print(aid,"Hellllllllllllopppppppppp\n\n\n")
        self.fields['owner'].required = False
        self.fields['agent'].required = False
        self.fields['date'].required = False
        
        #self.fields['property'].queryset = Property.objects.filter(status='for_lease')
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class BuySellTransactionForm(ModelForm):
    class Meta:
        model = BuySellTransaction
        fields = '__all__'
        widgets = {'owner': forms.HiddenInput(),'date':DateInput(),'agent': forms.HiddenInput(),'date': forms.HiddenInput()}
        

    def __init__(self,*args, **kwargs):
        super(BuySellTransactionForm, self).__init__(*args, **kwargs)        
        # self.request = kwargs.pop('request', None)
        # username = str(request.user)
        # agent = Agent.objects.get(username=username)
        # aid = agent.agent_id
        # print(aid,"Hellllllllllllopppppppppp\n\n\n")
        self.fields['owner'].required = False
        self.fields['agent'].required = False
        self.fields['date'].required = False
        
        #self.fields['property'].queryset = Property.objects.filter(status='for_lease')
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


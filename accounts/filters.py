import django_filters
from django_filters import DateFilter
from .models import *
from django.forms.widgets import DateTimeInput
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class PropertyFilter(django_filters.FilterSet):
    Amountgt = django_filters.NumberFilter(field_name='amount', lookup_expr='gt')
    Amountlt = django_filters.NumberFilter(field_name='amount', lookup_expr='lt')
    Sizegt = django_filters.NumberFilter(field_name='size',lookup_expr='gt')
    Sizelt = django_filters.NumberFilter(field_name='size',lookup_expr='lt')
    class Meta:
        model = Property      
        fields = ['property_id','no_of_bedrooms','status','type','size']


class TransactionFilter(django_filters.FilterSet):
    Date_start=DateFilter(field_name="date",lookup_expr='gte')
    Date_end=DateFilter(field_name="date",lookup_expr='lte')
    class Meta:
        model = BuySellTransaction     
        fields = ['property','buyer','owner']
        widgets = {'date':DateInput()}


class RentFilter(django_filters.FilterSet):
    Date_st=DateFilter(field_name="date",lookup_expr='gte')
    Date_e=DateFilter(field_name="date",lookup_expr='lte')
    class Meta:
        model = RentTransaction    
        fields = ['property','tenant','owner']
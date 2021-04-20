import django_filters
from .models import *

class PropertyFilter(django_filters.FilterSet):
    Amountgt = django_filters.NumberFilter(field_name='amount', lookup_expr='gt')
    Amountlt = django_filters.NumberFilter(field_name='amount', lookup_expr='lt')
    Sizegt = django_filters.NumberFilter(field_name='size',lookup_expr='gt')
    Sizelt = django_filters.NumberFilter(field_name='size',lookup_expr='lt')
    class Meta:
        model = Property      
        fields = ['property_id','no_of_bedrooms','status','type','size']
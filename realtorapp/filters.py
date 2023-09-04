import django_filters   
from .models import product

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = product
        fields = ['type_house' , 'price' , 'sell_type' , 'location' ,
                  'number_kitchen' , 'number_bedroom' , 'number_bathroom']
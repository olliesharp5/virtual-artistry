import django_filters
from .models import Art

class ArtFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Art
        fields = ['artist', 'condition', 'min_price', 'max_price']
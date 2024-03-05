import django_filters
from .models import Art

class ArtFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Art
        fields = ['artist', 'condition', 'price_min', 'price_max']

    def __init__(self, *args, **kwargs):
        super(ArtFilter, self).__init__(*args, **kwargs)
        self.filters['artist'].extra.update(
            {'empty_label': 'Any'}
        )
        self.filters['condition'].extra.update(
            {'empty_label': 'Any'}
        )
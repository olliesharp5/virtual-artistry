import django_filters
from artists.models import UserProfile
from .models import Art

class DisplayNameChoiceFilter(django_filters.ChoiceFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra['choices'] = [(userprofile.display_name, userprofile.display_name) for userprofile in UserProfile.objects.filter(role='AR')]

    def filter(self, qs, value):
        if value:
            return qs.filter(artist__display_name=value)
        return qs

class ArtFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    artist = DisplayNameChoiceFilter()

    class Meta:
        model = Art
        fields = ['artist', 'condition', 'price_min', 'price_max']

    def __init__(self, *args, **kwargs):
        super(ArtFilter, self).__init__(*args, **kwargs)
        self.filters['condition'].extra.update(
            {'empty_label': 'Any'}
        )
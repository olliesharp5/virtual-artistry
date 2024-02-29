import django_filters
from .models import ArtistProfile

class ArtistProfileFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='istartswith')

    class Meta:
        model = ArtistProfile
        fields = ['name']
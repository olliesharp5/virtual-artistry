import django_filters
from .models import ArtistProfile

class ArtistProfileFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate a list of tuples for all uppercase letters from A to Z that have existing artists
        self.filters['first_letter'].extra.update(
            {
                'choices': [(chr(i), chr(i)) for i in range(65, 91) if self.queryset.filter(name__istartswith=chr(i)).exists()],
                 'empty_label': None,
            }
        )

    first_letter = django_filters.ChoiceFilter(method='filter_by_first_letter')

    class Meta:
        model = ArtistProfile
        fields = ['first_letter']

    def filter_by_first_letter(self, queryset, name, value):
        return queryset.filter(name__istartswith=value)

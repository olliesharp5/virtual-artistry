from django.contrib import admin
from .models import Art, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Art)
class ArtworkAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('about',)

# Register your models here.

admin.site.register(Review)
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Art, Review, Like

@admin.register(Art)
class ArtworkAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('about',)

# Register your models here.

admin.site.register(Review)

admin.site.register(Like)
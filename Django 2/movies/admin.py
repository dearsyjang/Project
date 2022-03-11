from django.contrib import admin
from . models import Movie

# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    list_diplay = ('pk', 'title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description', 'created_at', 'updated_at')

admin.site.register(Movie)
from django.contrib import admin
from movies.models import Movie, Comment

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
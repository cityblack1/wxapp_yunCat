from django.contrib import admin

from .models import CatImage


class CatImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'status', 'like_nums' )

admin.site.register(CatImage, CatImageAdmin)
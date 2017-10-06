from django.contrib import admin

from .models import FeedBack, Contact


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('content', 'created', 'title')


admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Contact, ContactAdmin)
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Delivery

class DeliveryAdmin(TranslationAdmin):
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'descriptions', 'banner_image'),
        }),
        ('Trust Information', {
            'fields': ('trust_title', 'trust_descriptions', 'trust_descriptions2', 'trust_image'),
        }),
    )

admin.site.register(Delivery, DeliveryAdmin)

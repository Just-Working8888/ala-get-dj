from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from .models import Partners, LocalTaxi, PartnersSlider

class PartnersAdmin(TranslationAdmin):
    list_display = ('title', 'title2', 'descriptions', 'become_title', 'local_title')
    search_fields = ('title', 'descriptions', 'become_title', 'local_title')

class LocalTaxiAdmin(TranslationAdmin):
    list_display = ('title', 'image_display')
    search_fields = ('title',)

    def image_display(self, obj):
        return format_html('<img src="{}" height="50"/>'.format(obj.image.url))

    image_display.short_description = 'Image'

class PartnersSliderTaxiAdmin(TranslationAdmin):
    list_display = ('title', )



admin.site.register(Partners, PartnersAdmin)
admin.site.register(LocalTaxi, LocalTaxiAdmin)
admin.site.register(PartnersSlider,PartnersSliderTaxiAdmin)
from modeltranslation.translator import register, TranslationOptions
from .models import Delivery


@register(Delivery)
class DeliveryTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', 'trust_title', 'trust_descriptions', 'trust_descriptions2')



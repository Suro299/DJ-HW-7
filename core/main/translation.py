from .models import ActivCarusel, Carusel, FeaturesItems, CategoryItems, ActiveCategoryItems
from modeltranslation.translator import register, TranslationOptions

@register(ActivCarusel)
class ActivCaruselTranslationOptions(TranslationOptions):
    fields = ["title", "about_title", "about", "button_text"]


@register(Carusel)
class CaruselTranslationOptions(TranslationOptions):
    fields = ["title", "about_title", "about", "button_text"]


@register(FeaturesItems)
class FeaturesItemsTranslationOptions(TranslationOptions):
    fields = ["description", "button_text"]
    
    
@register(CategoryItems)
class CategoryItemsTranslationOptions(TranslationOptions):
    fields = ["description", "button_text"]

@register(ActiveCategoryItems)
class ActiveCategoryItemsTranslationOptions(TranslationOptions):
    fields = ["description", "button_text"]
    
    
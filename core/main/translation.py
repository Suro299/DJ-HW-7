from .models import Carusel, FeaturesItems, CategoryItems, ActiveCategoryItems, ProductSubCategory, ProductCategory
from modeltranslation.translator import register, TranslationOptions


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

@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ["name",]
    
@register(ProductSubCategory)
class ProductSubCategoryTranslationOptions(TranslationOptions):
    fields = ["name",] 
    
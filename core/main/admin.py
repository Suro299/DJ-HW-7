from django.contrib import admin
from .models import Carusel, FeaturesItems, Category, CategoryItems, ActiveCategory, ActiveCategoryItems
from .models import ProductCategory, ProductSubCategory

from .models import Contact
from modeltranslation.admin import TranslationAdmin

class CaruselAdmin(TranslationAdmin):
    pass

class FeaturesItemsAdmin(TranslationAdmin):
    pass

class CategoryItemsAdmin(TranslationAdmin):
    pass

class ActiveCategoryItemsAdmin(TranslationAdmin):
    pass

class ProductCategoryAdmin(TranslationAdmin):
    pass

class ProductSubCategoryAdmin(TranslationAdmin):
    pass




admin.site.register(Carusel) 
admin.site.register(FeaturesItems)

admin.site.register(Category)
admin.site.register(CategoryItems)

admin.site.register(ActiveCategory)
admin.site.register(ActiveCategoryItems)

admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)

admin.site.register(Contact)


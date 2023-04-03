from django.contrib import admin
from .models import Carusel, ActivCarusel, FeaturesItems, Category, CategoryItems, ActiveCategory, ActiveCategoryItems
from .models import Contact
from modeltranslation.admin import TranslationAdmin

class CaruselAdmin(TranslationAdmin):
    pass

class ActivCaruselAdmin(TranslationAdmin):
    pass

class FeaturesItemsAdmin(TranslationAdmin):
    pass

class CategoryItemsAdmin(TranslationAdmin):
    pass

class ActiveCategoryItemsAdmin(TranslationAdmin):
    pass



admin.site.register(Carusel) 
admin.site.register(ActivCarusel) 
admin.site.register(FeaturesItems)

admin.site.register(Category)
admin.site.register(CategoryItems)

admin.site.register(ActiveCategory)
admin.site.register(ActiveCategoryItems)

admin.site.register(Contact)


from django.contrib import admin
from .models import Carusel, FeaturesItems, Category, CategoryItems, ActiveCategory, ActiveCategoryItems
from .models import ProductCategory, ProductSubCategory, ShopProd, RecommendedItems, AdminPosts

from .models import Contact, UserComments
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

class ShopProdAdmin(TranslationAdmin):
    pass

class RecommendedItemsAdmin(TranslationAdmin):
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
admin.site.register(ShopProd)
admin.site.register(RecommendedItems)
admin.site.register(AdminPosts)
admin.site.register(UserComments)

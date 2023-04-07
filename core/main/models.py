from django.db import models


# =========================================================================================
#                                       INDEX
# =========================================================================================

class Carusel(models.Model):
    title = models.CharField("Title", max_length = 50)
    about_title = models.CharField("About Title", max_length = 50)
    about = models.TextField("About")
    button_text = models.CharField("Button Text", max_length = 57)
    img = models.ImageField("Image")
    subimge = models.ImageField("Sub Image")
    
    
    def __str__(self):
        return self.title

class FeaturesItems(models.Model):
    price = models.PositiveBigIntegerField("Item Price")
    img = models.ImageField("Item Image")
    description = models.CharField("Item Description", max_length= 100)
    button_text = models.CharField("Item Button Text", max_length = 50)
    sub_img = models.ImageField("Sub image", blank = True)
    
    def __str__(self) -> str:
        return self.description + f" ({self.id})"
    
    
class Category(models.Model):
    name = models.CharField("Category Name", max_length = 20)
    
    def __str__(self):
        return self.name
    
        
class CategoryItems(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    price = models.PositiveBigIntegerField("Item Price")
    img = models.ImageField("Item Image")
    description = models.CharField("Item Description", max_length= 100)
    button_text = models.CharField("Item Button Text", max_length = 50)
    
    def __str__(self) -> str:
        return f"{self.category} || {self.description} || ({self.id})"
    

class ActiveCategory(models.Model):
    name = models.CharField("Category Name", max_length = 20)
    
    def __str__(self):
        return self.name
    
class ActiveCategoryItems(models.Model):
    
    price = models.PositiveBigIntegerField("Item Price")
    img = models.ImageField("Item Image")
    description = models.CharField("Item Description", max_length= 100)
    button_text = models.CharField("Item Button Text", max_length = 50)
    
    def __str__(self) -> str:
        return f"{self.description} || ({self.id})"
    
    
    
class Contact(models.Model):
    name = models.CharField("Name", max_length = 50)
    email = models.EmailField("Email")
    subject = models.CharField("Subject", max_length = 50)
    message = models.TextField("Message")
    
    def __str__(self) -> str:
        return f"{self.name} || {self.subject}"
    
class RecommendedItems(models.Model):
    price = models.PositiveBigIntegerField("Item Price")
    img = models.ImageField("Item Image")
    description = models.CharField("Item Description", max_length= 100)
    button_text = models.CharField("Item Button Text", max_length = 50)
    
    def __str__(self) -> str:
        return f"{self.description} || ({self.id})"
    
    
    
# =========================================================================================
#                                       (/inc) Nav
# =========================================================================================
    
class ProductCategory(models.Model):
    name = models.CharField("Product Category", max_length = 50)
    
    def __str__(self):
        return self.name
    
    
class ProductSubCategory(models.Model):
    category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE, related_name="category")
    name = models.CharField("Product Name", max_length = 50)
    
    def __str__(self):
        return f"{self.name} || {self.category.name}"
    

# =========================================================================================
#                                       Shop
# =========================================================================================
 
class ShopProd(models.Model):
    category = models.ForeignKey("ProductSubCategory", on_delete=models.PROTECT)
    
    price = models.PositiveBigIntegerField("Item Price")
    img = models.ImageField("Item Image")
    description = models.CharField("Item Description", max_length= 255)
    button_text = models.CharField("Item Button Text", max_length = 50)
    
    def __str__(self) -> str:
        return f"{self.category} || {self.description} || ({self.id})"
    
    
    
# =========================================================================================
#                                       Blog Single
# =========================================================================================


class AdminPosts(models.Model):
    admin_name = models.CharField("Admin Name", max_length = 255, default = "None")
    title = models.CharField("Post Title", max_length = 150)
    img = models.ImageField("Post Image")
    description = models.TextField("Post Description")
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)
    
    def __str__(self) -> str:
        return f"{self.admin_name} || {self.title} || {self.date}|| {self.time}"





class UserComments(models.Model):
    username = models.CharField("User Name", max_length = 255)
    message = models.TextField("User Message")
    img = models.ImageField("User Image")
    email = models.EmailField("User Email")
    
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)
    
        
    def __str__(self) -> str:
        return f"{self.username} || {self.date}|| {self.time}"

from django.db import models

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
    category = models.ForeignKey("Category", on_delete=models.PROTECT)
    
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
    
    
    
class ProductCategory(models.Model):
    name = models.CharField("Product Category", max_length = 50)

    def __str__(self):
        return self.name
    
    
class ProductSubCategory(models.Model):
    category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE, related_name="category")
    name = models.CharField("Product Name", max_length = 50)
    
    def __str__(self):
        return f"{self.name} || {self.category.name}"
    
    
 
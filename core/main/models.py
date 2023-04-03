from django.db import models

class ActivCarusel(models.Model):
    title = models.CharField("Activ Title", max_length = 50)
    about_title = models.CharField("Activ About Title", max_length = 50)
    about = models.TextField("Activ About")
    button_text = models.CharField("Activ Button Text", max_length = 57)
    img = models.ImageField("Activ Image")
    subimge = models.ImageField("Activ Sub Image")
    
    def __str__(self):
        return self.title

class Carusel(models.Model):
    title = models.CharField("Title", max_length = 50)
    about_title = models.CharField("About Title", max_length = 50)
    about = models.TextField("About")
    button_text = models.CharField("Button Text", max_length = 57)
    img = models.ImageField("Image")
    subimge = models.ImageField("Sub Image")
    
    
    def __str__(self):
        return self.title
    
    
class A(models.Model):
    
    title = models.CharField("Title", max_length = 50)
    
    div1_price = models.CharField("div-1 Title", max_length = 50)
    div1_about = models.TextField("div-1 About")
    div1_img = models.ImageField("div-1 Img")

    div2_price = models.CharField("div-2 Title", max_length = 50)
    div2_about = models.TextField("div-2 About")
    div2_img = models.ImageField("div-2 Img")
    
    div3_price = models.CharField("div-3 Title", max_length = 50)
    div3_about = models.TextField("div-3 About")
    div3_img = models.ImageField("div-3 Img")
    
    div4_price = models.CharField("div-4 Title", max_length = 50)
    div4_about = models.TextField("div-4 About")
    div4_img = models.ImageField("div-4 Img")
    
    def __str__(self):
        return self.title
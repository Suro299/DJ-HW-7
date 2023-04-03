from django.shortcuts import render, redirect
from .models import Carusel, ActivCarusel, FeaturesItems, Category, CategoryItems, ActiveCategory, ActiveCategoryItems
from .models import Contact 

from .forms import MyUserCreationForm, ContactModelForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    features_items = FeaturesItems.objects.all()[:6]
    carusel_list = Carusel.objects.all()
    activ_carusel = ActivCarusel.objects.all()[0]
    category_list = Category.objects.all()
    category_items = CategoryItems.objects.all()
    
    active_category = ActiveCategory.objects.all()[0]
    active_category_item = ActiveCategoryItems.objects.all()[0]
    
    return render(request, "main/index.html", context = {
        "carusel_list": carusel_list,
        "activ_carusel": activ_carusel,
        "features_items": features_items,
        
        "category_list": category_list,
        "category_items": category_items,
        
        "active_category": active_category,
        "active_category_item": active_category_item
    })


def ftf(request):
    return render(request, "main/404.html")


def blog_single(request):
    return render(request, "main/blog-single.html")
    
    
def blog(request):
    return render(request, "main/blog.html")
    
    
def cart(request):
    return render(request, "main/cart.html")
    
    
def checkout(request):
    return render(request, "main/checkout.html")
    
    
def contact_us(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect("contact_us")
    else:
        form = ContactModelForm()
        
        
    return render(request, "main/contact-us.html", context = {
        "form": form
    })
    
def product_details(request):
    return render(request, "main/product-details.html")


def shop(request):
    return render(request, "main/shop.html")
  

    
  
  


def register_request(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = MyUserCreationForm()
    return render(request, 'main/reg.html', {'form': form})





def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")


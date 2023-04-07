from django.shortcuts import render, redirect


from .models import Carusel, FeaturesItems, Category, CategoryItems, ActiveCategory, ActiveCategoryItems
from .models import Contact, ProductCategory, ShopProd, RecommendedItems, AdminPosts, UserComments

from .forms import MyUserCreationForm, ContactModelForm, UserMessageModelForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    features_items = FeaturesItems.objects.all()[:6]
    activ_carusel = Carusel.objects.all()[0] 
    carusel_list = Carusel.objects.all()[1:]
    
    category_list = Category.objects.all()
    category_items = CategoryItems.objects.all()
    
    active_category = ActiveCategory.objects.all()[0]
    active_category_item = ActiveCategoryItems.objects.all()
    product_category_list = ProductCategory.objects.all()
    
    activ_rec_prod = RecommendedItems.objects.all()[:3:]
    rec_prod = RecommendedItems.objects.all()[3:]
    
    if request.method == "POST":
        return redirect("shop")
        
    
    return render(request, "main/index.html", context = {
        "carusel_list": carusel_list,
        "activ_carusel": activ_carusel,
        "features_items": features_items,
        "category_list": category_list,
        "category_items": category_items,
        "active_category": active_category,
        "active_category_item": active_category_item,
        "product_category_list": product_category_list,
      
        "rec_prod": rec_prod,
        "activ_rec_prod": activ_rec_prod
    
    })


def ftf(request):
    return render(request, "main/404.html")


def blog_single(request):
    product_category_list = ProductCategory.objects.all()
    admin_post = AdminPosts.objects.all()
    last_admin_post = admin_post[len(admin_post)-2]
    admin_post = admin_post[len(admin_post)-1]
    messages_list = UserComments.objects.all()
    
    if request.method == "POST":
        form = UserMessageModelForm(request.POST, request.FILES)
        if form.is_valid():
            UserComments.objects.create(**form.cleaned_data)
            return redirect("blog_single")
        print("asdasdasdasdasdasddassssssssssssssssssssssssssssssssssssssssssssssssssssss")
        
    else:
        form = UserMessageModelForm()
        
    return render(request, "main/blog-single.html", context = {
        "product_category_list": product_category_list,
        "admin_post": admin_post,
        "last_admin_post": last_admin_post,
        "messages_list": messages_list,
        
        "form": form
    })
    
    
    
    
def blog(request):
    
    return render(request, "main/blog.html",)
    
    
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
    product_category_list = ProductCategory.objects.all()
    prod_list = ShopProd.objects.all()
    max_min = [0, 500000]
    if request.method == 'POST':
        option = request.POST.get('cat_btn')  
        if option != None:
            prod_list = prod_list.filter(category__name__icontains=option)
        else:
            price_range = request.POST.get("price_range")
            max_min= price_range.split(",")

    return render(request, "main/shop.html", context = {
        "product_category_list": product_category_list,
        "prod_list": prod_list,
        "min": int(max_min[0]),
        "max": int(max_min[1])
    })
  
    
    

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






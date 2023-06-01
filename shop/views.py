from django.contrib import messages
from django.shortcuts import render
from .models import Product, Order 
from django.core.paginator import Paginator
from .forms import UserRegistrationForm 
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect 
from .models import Contact
from django.http import HttpResponse
from PIL import Image

# Create your views here.

#Index code done by Martina
@csrf_protect
def index(request):
    product_objects = Product.objects.all()
# search function for the user to be able to search for product, done by Martina
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)


# paginator code done by Martina. Each page has 4 products.
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})

# Detail viex code, the user is able to see the detail view of the product,
# done by Martina

@csrf_protect
def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})

  
# Checkout function done by Martina,
# before the code there is a login_required decorator, 
# when user wants to checkout he needs to fist login.
# Another decorator is the csrf to protect
@login_required
@csrf_protect
def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        zipcode = request.POST.get('zipcode', "")
        region = request.POST.get('region', "")
        total = request.POST.get('total', "")
        order = Order(items=items, name=name, email=email,
                      address=address, city=city, zipcode=zipcode, total=total)
        order.save()

    return render(request, 'shop/checkout.html')

# User registration function done by Jovan

@csrf_protect
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return redirect('login')
    user_form = UserRegistrationForm()
    return render(request, 'shop/register.html', {'user_form': user_form})


# Contact function done by Jeremy
@csrf_protect
def contact(request):
     if request.method == 'POST':
         name = request.POST.get('name', "")
         email = request.POST.get('email', "")
         subject = request.POST.get('subject', "")
         message = request.POST.get('message', "")
         query = Contact(name=name, email=email, subject=subject, message=message)
         query.save

     return render(request, 'contact.html')




# Account locked fucntion done by Martina. This is part of the Brute force management,
# when user get lockout due to the multiple failed login attempts, user will redirect to the accountLoged page
@csrf_protect
def accountLocked(request):
    return render(request, 'accountLocked.html')


   
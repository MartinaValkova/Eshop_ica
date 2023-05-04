from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator
from .forms import UserRegistrationForm


# Create your views here.


def index(request):
    product_objects = Product.objects.all()
    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # paginator code
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_objects': product_objects})

    # Detail viex code


def detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': product_object})

   # Checkout
# @login-required


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

# User registeration


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return redirect('index')
    user_form = UserRegistrationForm()
    return render(request, 'shop/register.html', {'user_form': user_form})


def contact(request):
    return render(request, 'contact.html')

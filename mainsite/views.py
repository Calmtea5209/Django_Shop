from django.shortcuts import get_object_or_404, render
from .models import Category,Product
from cart.forms import CartAddProductForm
# Create your views here.

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category_slug: #類別頁面
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    return render(request,'mainsite/product/list.html',locals())

def product_detail(request,product_id,slug):
    product = get_object_or_404(Product,id=product_id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'mainsite/product/detail.html',locals())
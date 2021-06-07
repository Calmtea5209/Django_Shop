from decimal import Decimal

from django.conf import settings

from mainsite.models import Product


class Cart(object):
    def __init__(self, request): #初始化

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:   #建立空cart
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):  #增加、更新產品

        product_id = str(product.id)
        if product_id not in self.cart: #初始化
            self.cart[product_id] = {'quantity': 0,'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # 更新session
        self.session[settings.CART_SESSION_ID] = self.cart
        # 確保儲存
        self.session.modified = True

    def remove(self, product): #刪除product
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        #取得所有product
        product_ids = self.cart.keys() #list
        #將produtct加到cart
        products = Product.objects.filter(id__in=product_ids) #id__in可以找誰在list中
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):

        # {% with total_items=cart|length %}
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        #刪除cart
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

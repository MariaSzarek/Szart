from django.contrib import admin
from .models import Product, Like, Cart, CartItem

admin.site.register(Product)
admin.site.register(Like)
admin.site.register(Cart)
admin.site.register(CartItem)
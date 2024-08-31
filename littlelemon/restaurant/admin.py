from django.contrib import admin

# Register your models here.
from .models import Menu
from .models import Booking
from .models import Registering

# Other ports
from .models import Category, MenuItem, Cart, Order, OrderItem


admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(Registering)



# Other Admin Items

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'featured')
    search_fields = ('title', 'category__title')
    list_filter = ('category', 'featured')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'menuitem', 'quantity', 'unit_price', 'price')
    search_fields = ('user__username', 'menuitem__title')
    list_filter = ('user', 'menuitem')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_crew', 'status', 'total', 'date')
    search_fields = ('user__username', 'delivery_crew__username', 'status')
    list_filter = ('status', 'date', 'user', 'delivery_crew')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menuitem', 'quantity', 'price')
    search_fields = ('order__id', 'menuitem__title')
    list_filter = ('order', 'menuitem')






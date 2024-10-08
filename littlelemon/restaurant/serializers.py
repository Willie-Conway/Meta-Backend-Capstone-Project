from rest_framework import serializers
from django.contrib.auth.models import User
from decimal import Decimal

from .models import Booking, Category, MenuItem, Cart, Order, OrderItem, Menu, Registering
from django.contrib.auth.hashers import make_password

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    # category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'category', 'featured']


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )


    def validate(self, attrs):
        attrs['price'] = attrs['quantity'] * attrs['unit_price']
        return attrs

    class Meta:
        model = Cart
        fields = ['user', 'menuitem', 'unit_price', 'quantity', 'price']
        extra_kwargs = {
            'price': {'read_only': True}
        }


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'menuitem', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):

    orderitem = OrderItemSerializer(many=True, read_only=True, source='order')

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew',
                  'status', 'date', 'total', 'orderitem']


class UserSerilializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'menu_item_description', 'image']
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'first_name', 'reservation_date', 'reservation_slot']


class RegisteringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registering
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is not read in responses
            'date_joined': {'read_only': True},  # Ensure date_joined is read-only
        }

    def create(self, validated_data):
        # Create and return a new `Registering` instance, given the validated data
        # Hash the password before saving
        password = validated_data.pop('password')
        user = Registering.objects.create(**validated_data)
        user.password = make_password(password)  # Hash the password
        user.save()
        return user
        

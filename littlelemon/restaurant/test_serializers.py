from decimal import Decimal
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Booking, Category, MenuItem, Cart, Order, OrderItem, Menu, Registering
from .serializers import (
    CategorySerializer, MenuItemSerializer, CartSerializer, 
    OrderItemSerializer, OrderSerializer, UserSerilializer, 
    MenuSerializer, BookingSerializer, RegisteringSerializer
)

class TestSerializers(APITestCase):

    def setUp(self):
        # Create some test data
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
        self.category = Category.objects.create(title='Beverages', slug='beverages')
        self.menu_item = MenuItem.objects.create(title='Coffee', price=Decimal('2.50'), category=self.category, featured=True)
        self.cart = Cart.objects.create(user=self.user, menuitem=self.menu_item, unit_price=Decimal('2.50'), quantity=2)
        self.order = Order.objects.create(user=self.user, delivery_crew=self.user, status='Pending', date='2024-08-31', total=Decimal('5.00'))
        self.order_item = OrderItem.objects.create(order=self.order, menuitem=self.menu_item, quantity=2, price=Decimal('5.00'))
        self.menu = Menu.objects.create(name='Special Menu', price=Decimal('10.00'), menu_item_description='A special menu item', image='path/to/image.jpg')
        self.booking = Booking.objects.create(first_name='John', reservation_date='2024-09-01', reservation_slot='18:00')
        self.registering = Registering.objects.create(username='registeruser', email='registeruser@example.com', password='password123', first_name='Register', last_name='User')

    def test_category_serializer(self):
        serializer = CategorySerializer(instance=self.category)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'slug']))
        self.assertEqual(data['title'], 'Beverages')

    def test_menu_item_serializer(self):
        serializer = MenuItemSerializer(instance=self.menu_item)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'price', 'category', 'featured']))
        self.assertEqual(data['title'], 'Coffee')
        self.assertEqual(data['category'], self.category.id)

    def test_cart_serializer(self):
        serializer = CartSerializer(instance=self.cart)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['user', 'menuitem', 'unit_price', 'quantity', 'price']))
        self.assertEqual(data['price'], str(self.cart.quantity * self.cart.unit_price))

    def test_order_item_serializer(self):
        serializer = OrderItemSerializer(instance=self.order_item)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['order', 'menuitem', 'quantity', 'price']))
        self.assertEqual(data['quantity'], 2)
        self.assertEqual(data['price'], str(self.order_item.price))

    def test_order_serializer(self):
        serializer = OrderSerializer(instance=self.order)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'user', 'delivery_crew', 'status', 'date', 'total', 'orderitem']))
        self.assertEqual(data['status'], 'Pending')
        self.assertEqual(len(data['orderitem']), 1)

    def test_user_serializer(self):
        serializer = UserSerilializer(instance=self.user)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'username', 'email']))
        self.assertEqual(data['username'], 'testuser')

    def test_menu_serializer(self):
        serializer = MenuSerializer(instance=self.menu)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'price', 'menu_item_description', 'image']))
        self.assertEqual(data['name'], 'Special Menu')

    def test_booking_serializer(self):
        serializer = BookingSerializer(instance=self.booking)
        data = serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'first_name', 'reservation_date', 'reservation_slot']))
        self.assertEqual(data['first_name'], 'John')

    def test_registering_serializer_create(self):
        serializer = RegisteringSerializer(data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'first_name': 'New',
            'last_name': 'User'
        })
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'newuser')
        self.assertNotEqual(user.password, 'newpassword123')  # Password should be hashed

    def test_registering_serializer_no_password_read(self):
        serializer = RegisteringSerializer(instance=self.registering)
        data = serializer.data
        self.assertNotIn('password', data)  # Password should not be in the serialized data

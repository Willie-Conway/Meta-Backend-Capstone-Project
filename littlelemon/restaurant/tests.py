from datetime import datetime
from decimal import Decimal
from django.forms import ValidationError
from django.test import TestCase

# Create your tests here.

# TESTS FOR SERIALIZERS and VIEWS

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User, Group
from .models import Category, Menu, MenuItem, Cart, Order, OrderItem, Booking, Registering
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    CartSerializer,
    OrderItemSerializer,
    OrderSerializer,
    UserSerilializer
)
import json
from django.utils.dateparse import parse_date


# VIEWS UNIT TESTS

class ViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Create test users
        self.superuser = User.objects.create_superuser(username='admin', password='admin', email='admin@example.com')
        self.manager = User.objects.create_user(username='manager', password='manager', email='manager@example.com')
        self.delivery_crew = User.objects.create_user(username='delivery', password='delivery', email='delivery@example.com')
        self.customer = User.objects.create_user(username='customer', password='customer', email='customer@example.com')
        
        # Create groups
        self.manager_group = Group.objects.create(name='Manager')
        self.delivery_group = Group.objects.create(name='Delivery Crew')
        self.manager.groups.add(self.manager_group)
        self.delivery_crew.groups.add(self.delivery_group)
        
        # Create test data
        self.category = Category.objects.create(title="Beverages", slug="beverages")
        self.menu_item = MenuItem.objects.create(
            title="Coke",
            price=Decimal('1.99'),
            category=self.category,
            featured=True
        )
        self.cart = Cart.objects.create(
            user=self.customer,
            menuitem=self.menu_item,
            unit_price=Decimal('1.99'),
            quantity=2
        )
        self.order = Order.objects.create(user=self.customer, delivery_crew=None, status='Pending', date=datetime.today().date(), total=Decimal('3.98'))
        self.order_item = OrderItem.objects.create(
            order=self.order,
            menuitem=self.menu_item,
            quantity=2,
            price=Decimal('3.98')
        )

        # Authentication
        self.client.force_authenticate(user=self.customer)

        # Home
    def test_home_page(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        # About
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

        # Reservations
    def test_reservations_page(self):
        response = self.client.get('/reservations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')

        # Registrations
    def test_all_registrations_page(self):
        response = self.client.get('/all-registrations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrations.html')

    #     # Book
    # def test_book_page(self):
    #     response = self.client.get('/book/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'book.html')

    #     # Menu
    # def test_menu_page(self):
    #     response = self.client.get('/menu/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'menu.html')

    #     # Menu Display Menu Item
    # def test_display_menu_item(self):
    #     response = self.client.get(f'/menu-item/{self.menu_item.id}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'menu_item.html')

    #     # Bookings Post
    # def test_bookings_api_post(self):
    #     data = {
    #         'first_name': 'John',
    #         'reservation_date': '2024-08-30',
    #         'reservation_slot': '12:00'
    #     }
    #     response = self.client.post('/api/bookings/', data, format='json')
    #     self.assertEqual(response.status_code, 201)

    #     # Bookings Get
    # def test_bookings_api_get(self):
    #     response = self.client.get('/api/bookings/?date=2024-08-30')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json()), 1)

    #     # Registrations Post
    # def test_registrations_api_post(self):
    #     data = {
    #         'username': 'newuser',
    #         'email': 'newuser@example.com',
    #         'password': 'newpassword',
    #         'first_name': 'New',
    #         'last_name': 'User'
    #     }
    #     response = self.client.post('/api/registrations/', data, format='json')
    #     self.assertEqual(response.status_code, 201)

    #     # Categories
    # def test_categories_view(self):
    #     response = self.client.get('/api/categories/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    #     # Menu Items
    # def test_menu_items_view(self):
    #     response = self.client.get('/api/menu-items/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Cart
    # def test_cart_view(self):
    #     response = self.client.get('/api/cart/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Order
    # def test_order_view(self):
    #     response = self.client.get('/api/orders/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Single Order
    # def test_single_order_view(self):
    #     response = self.client.get(f'/api/orders/{self.order.id}/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Groups
    # def test_group_viewset_list(self):
    #     self.client.force_authenticate(user=self.superuser)
    #     response = self.client.get('/api/groups/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Delivery Crew
    # def test_delivery_crew_viewset_list(self):
    #     response = self.client.get('/api/delivery-crew/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_delivery_crew_viewset_create(self):
    #     self.client.force_authenticate(user=self.superuser)
    #     data = {'username': 'delivery'}
    #     response = self.client.post('/api/delivery-crew/', data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_delivery_crew_viewset_destroy(self):
    #     self.client.force_authenticate(user=self.superuser)
    #     data = {'username': 'delivery'}
    #     self.client.post('/api/delivery-crew/', data, format='json')
    #     response = self.client.delete('/api/delivery-crew/', data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


# # SERIALIZERS UNIT TEST

# class CategorySerializerTests(TestCase):

#     def setUp(self):
#         self.category = Category.objects.create(title="Beverages", slug="beverages")

#     def test_category_serializer(self):
#         serializer = CategorySerializer(self.category)
#         self.assertEqual(serializer.data, {
#             'id': self.category.id,
#             'title': self.category.title,
#             'slug': self.category.slug
#         })


# class MenuItemSerializerTests(TestCase):

#     def setUp(self):
#         self.category = Category.objects.create(title="Beverages", slug="beverages")
#         self.menu_item = MenuItem.objects.create(
#             title="Coke",
#             price=Decimal('1.99'),
#             category=self.category,
#             featured=True
#         )

#     def test_menu_item_serializer(self):
#         serializer = MenuItemSerializer(self.menu_item)
#         self.assertEqual(serializer.data, {
#             'id': self.menu_item.id,
#             'title': self.menu_item.title,
#             'price': str(self.menu_item.price),
#             'category': self.menu_item.category.id,
#             'featured': self.menu_item.featured
#         })


# class CartSerializerTests(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="testpassword")
#         self.category = Category.objects.create(title="Beverages", slug="beverages")
#         self.menu_item = MenuItem.objects.create(
#             title="Coke",
#             price=Decimal('1.99'),
#             category=self.category,
#             featured=True
#         )
#         self.cart = Cart.objects.create(
#             user=self.user,
#             menuitem=self.menu_item,
#             unit_price=Decimal('1.99'),
#             quantity=2
#         )

#     def test_cart_serializer_valid(self):
#         serializer = CartSerializer(self.cart)
#         self.assertEqual(serializer.data, {
#             'user': self.user.id,
#             'menuitem': self.menu_item.id,
#             'unit_price': str(self.cart.unit_price),
#             'quantity': self.cart.quantity,
#             'price': str(self.cart.price)
#         })

#     def test_cart_serializer_invalid(self):
#         data = {
#             'user': self.user.id,
#             'menuitem': self.menu_item.id,
#             'unit_price': 'invalid',
#             'quantity': 'invalid'
#         }
#         serializer = CartSerializer(data=data)
#         with self.assertRaises(ValidationError):
#             serializer.is_valid(raise_exception=True)


# class OrderItemSerializerTests(TestCase):

#     def setUp(self):
#         self.order = Order.objects.create(user=User.objects.create_user(username='testuser', password='testpassword'), total=Decimal('10.00'))
#         self.menu_item = MenuItem.objects.create(title="Coke", price=Decimal('1.99'), category=Category.objects.create(title="Beverages", slug="beverages"), featured=True)
#         self.order_item = OrderItem.objects.create(
#             order=self.order,
#             menuitem=self.menu_item,
#             quantity=2,
#             price=Decimal('3.98')
#         )

#     def test_order_item_serializer(self):
#         serializer = OrderItemSerializer(self.order_item)
#         self.assertEqual(serializer.data, {
#             'order': self.order.id,
#             'menuitem': self.menu_item.id,
#             'quantity': self.order_item.quantity,
#             'price': str(self.order_item.price)
#         })


# class OrderSerializerTests(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="testpassword")
#         self.category = Category.objects.create(title="Beverages", slug="beverages")
#         self.menu_item = MenuItem.objects.create(
#             title="Coke",
#             price=Decimal('1.99'),
#             category=self.category,
#             featured=True
#         )
#         self.order = Order.objects.create(user=self.user, delivery_crew=None, status='Pending', date='2024-08-30', total=Decimal('3.98'))
#         self.order_item = OrderItem.objects.create(
#             order=self.order,
#             menuitem=self.menu_item,
#             quantity=2,
#             price=Decimal('3.98')
#         )

#     def test_order_serializer(self):
#         serializer = OrderSerializer(self.order)
#         self.assertEqual(serializer.data, {
#             'id': self.order.id,
#             'user': self.user.id,
#             'delivery_crew': None,
#             'status': self.order.status,
#             'date': self.order.date.strftime('%Y-%m-%d'),
#             'total': str(self.order.total),
#             'orderitem': [{
#                 'order': self.order.id,
#                 'menuitem': self.menu_item.id,
#                 'quantity': self.order_item.quantity,
#                 'price': str(self.order_item.price)
#             }]
#         })


# class UserSerilializerTests(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", email="testuser@example.com", password="testpassword")

#     def test_user_serializer(self):
#         serializer = UserSerilializer(self.user)
#         self.assertEqual(serializer.data, {
#             'id': self.user.id,
#             'username': self.user.username,
#             'email': self.user.email
#         })
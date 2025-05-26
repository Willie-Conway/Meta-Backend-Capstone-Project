from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User, Group
from .models import Category, Menu, MenuItem, Cart, Order, OrderItem, Booking, Registering
from django.urls import reverse
from django.core import serializers
from datetime import datetime
import json

class ViewsTestCase(TestCase):

    def setUp(self):
        # Create test users
        self.admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')
        self.manager_user = User.objects.create_user(username='manager', email='manager@example.com', password='manager123')
        self.delivery_crew_user = User.objects.create_user(username='delivery_crew', email='delivery@example.com', password='delivery123')
        self.customer_user = User.objects.create_user(username='customer', email='customer@example.com', password='customer123')
        
        # Create groups
        self.manager_group, _ = Group.objects.get_or_create(name='Manager')
        self.delivery_crew_group, _ = Group.objects.get_or_create(name='Delivery Crew')
        self.manager_user.groups.add(self.manager_group)
        self.delivery_crew_user.groups.add(self.delivery_crew_group)

        # Create test data
        self.category = Category.objects.create(title='Beverages', slug='beverages')
        self.menu_item = MenuItem.objects.create(title='Coffee', price=2.50, category=self.category, featured=True)
        self.cart = Cart.objects.create(user=self.customer_user, menuitem=self.menu_item, unit_price=2.50, quantity=2)
        self.order = Order.objects.create(user=self.customer_user, delivery_crew=self.delivery_crew_user, status='Pending', date=datetime.today().date(), total=5.00)
        self.order_item = OrderItem.objects.create(order=self.order, menuitem=self.menu_item, quantity=2, price=5.00)
        self.menu = Menu.objects.create(name='Special Menu', price=10.00, menu_item_description='A special menu item', image='path/to/image.jpg')
        self.booking = Booking.objects.create(first_name='John', reservation_date=datetime.today().date(), reservation_slot='18:00')
        self.registering = Registering.objects.create(username='registeruser', email='registeruser@example.com', password='password123', first_name='Register', last_name='User')

        # Initialize APIClient
        self.client = APIClient()
    
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_reservations_page(self):
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)

    def test_bookings_page(self):
        response = self.client.get(reverse('bookings'))
        self.assertEqual(response.status_code, 200)

    def test_menu_page(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

    def test_display_menu_item(self):
        response = self.client.get(reverse('display_menu_item', args=[self.menu.id]))
        self.assertEqual(response.status_code, 200)

    def test_bookings_create(self):
        response = self.client.post(reverse('bookings'), data=json.dumps({
            'first_name': 'Jane',
            'reservation_date': '2024-09-01',
            'reservation_slot': '19:00'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_registrations_create(self):
        response = self.client.post(reverse('registrations'), data=json.dumps({
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'first_name': 'New',
            'last_name': 'User'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_categories_view(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(reverse('categories-list'))
        self.assertEqual(response.status_code, 200)

    def test_menu_items_view(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(reverse('menuitems-list'))
        self.assertEqual(response.status_code, 200)

    def test_single_menu_item_view(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(reverse('menuitem-detail', args=[self.menu_item.id]))
        self.assertEqual(response.status_code, 200)

    def test_cart_view(self):
        self.client.force_authenticate(user=self.customer_user)
        response = self.client.get(reverse('cart-list'))
        self.assertEqual(response.status_code, 200)

    def test_order_view(self):
        self.client.force_authenticate(user=self.customer_user)
        response = self.client.get(reverse('order-list'))
        self.assertEqual(response.status_code, 200)

    def test_single_order_view(self):
        self.client.force_authenticate(user=self.customer_user)
        response = self.client.get(reverse('order-detail', args=[self.order.id]))
        self.assertEqual(response.status_code, 200)

    def test_group_viewset_list(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(reverse('group-list'))
        self.assertEqual(response.status_code, 200)

    def test_delivery_crew_viewset_list(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(reverse('deliverycrew-list'))
        self.assertEqual(response.status_code, 200)

    def test_booking_list_view(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 200)

    def test_booking_detail_view(self):
        response = self.client.get(reverse('booking-detail', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)

    def test_registering_list_create_view(self):
        response = self.client.get(reverse('registering-list'))
        self.assertEqual(response.status_code, 200)

    def test_registering_detail_view(self):
        response = self.client.get(reverse('registering-detail', args=[self.registering.id]))
        self.assertEqual(response.status_code, 200)

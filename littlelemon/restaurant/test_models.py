from django.test import TestCase
from django.contrib.auth.models import User
from .models import Registering, Booking, Menu, Category, MenuItem, Cart, Order, OrderItem
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime

class RegisteringModelTestCase(TestCase):

    def setUp(self):
        self.user = Registering.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_registering_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.password.startswith('pbkdf2_sha256$'))  # Check if password is hashed
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')

    def test_registering_string_representation(self):
        self.assertEqual(str(self.user), 'testuser')


class BookingModelTestCase(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(
            first_name='John Doe',
            reservation_date=datetime.today().date(),
            reservation_slot=18
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.first_name, 'John Doe')
        self.assertEqual(self.booking.reservation_slot, 18)

    def test_booking_string_representation(self):
        self.assertEqual(str(self.booking), 'John Doe')


class MenuModelTestCase(TestCase):

    def setUp(self):
        self.menu = Menu.objects.create(
            name='Special Dish',
            price=12,
            menu_item_description='A special dish with a unique taste',
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

    def test_menu_creation(self):
        self.assertEqual(self.menu.name, 'Special Dish')
        self.assertEqual(self.menu.price, 12)
        self.assertEqual(self.menu.menu_item_description, 'A special dish with a unique taste')
        self.assertTrue(self.menu.image.name.startswith('menu_items/test_image.jpg'))

    def test_menu_string_representation(self):
        self.assertEqual(str(self.menu), 'Special Dish')


class CategoryModelTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title='Appetizers',
            slug='appetizers'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.title, 'Appetizers')
        self.assertEqual(self.category.slug, 'appetizers')

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), 'Appetizers')


class MenuItemModelTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title='Appetizers',
            slug='appetizers'
        )
        self.menu_item = MenuItem.objects.create(
            title='Spring Roll',
            price=5.50,
            featured=True,
            category=self.category
        )

    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.title, 'Spring Roll')
        self.assertEqual(self.menu_item.price, 5.50)
        self.assertEqual(self.menu_item.category, self.category)
        self.assertTrue(self.menu_item.featured)

    def test_menu_item_string_representation(self):
        self.assertEqual(str(self.menu_item), 'Spring Roll')


class CartModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='cartuser', password='password123')
        self.category = Category.objects.create(title='Beverages', slug='beverages')
        self.menu_item = MenuItem.objects.create(title='Coffee', price=2.50, featured=True, category=self.category)
        self.cart = Cart.objects.create(
            user=self.user,
            menuitem=self.menu_item,
            quantity=3,
            unit_price=2.50,
            price=7.50
        )

    def test_cart_creation(self):
        self.assertEqual(self.cart.user, self.user)
        self.assertEqual(self.cart.menuitem, self.menu_item)
        self.assertEqual(self.cart.quantity, 3)
        self.assertEqual(self.cart.unit_price, 2.50)
        self.assertEqual(self.cart.price, 7.50)

    def test_cart_unique_together(self):
        with self.assertRaises(Exception):
            Cart.objects.create(
                user=self.user,
                menuitem=self.menu_item,
                quantity=5,
                unit_price=2.50,
                price=12.50
            )


class OrderModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='orderuser', password='password123')
        self.delivery_crew = User.objects.create_user(username='delivery_crew', password='password123')
        self.order = Order.objects.create(
            user=self.user,
            delivery_crew=self.delivery_crew,
            status=1,  # Assuming 1 means 'Pending'
            total=15.00,
            date=datetime.today().date()
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.delivery_crew, self.delivery_crew)
        self.assertEqual(self.order.status, 1)
        self.assertEqual(self.order.total, 15.00)

    def test_order_string_representation(self):
        self.assertEqual(str(self.order), f'Order by {self.user.username} on {self.order.date}')


class OrderItemModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='orderuser', password='password123')
        self.menu_item = MenuItem.objects.create(title='Pizza', price=8.00, featured=True, category=Category.objects.create(title='Main Course', slug='main-course'))
        self.order = Order.objects.create(
            user=self.user,
            delivery_crew=self.user,
            status=1,
            total=8.00,
            date=datetime.today().date()
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            menuitem=self.menu_item,
            quantity=1,
            price=8.00
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.menuitem, self.menu_item)
        self.assertEqual(self.order_item.quantity, 1)
        self.assertEqual(self.order_item.price, 8.00)

    def test_order_item_unique_together(self):
        with self.assertRaises(Exception):
            OrderItem.objects.create(
                order=self.order,
                menuitem=self.menu_item,
                quantity=2,
                price=16.00
            )


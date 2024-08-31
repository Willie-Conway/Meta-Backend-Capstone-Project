from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings/', views.bookings, name='bookings'),
    path('book/', views.book, name='book'),
    path('register/', views.register, name='register'), # Ensure this matches the registration form action
    path('registrations/', views.registrations, name="registrations"), # Ensure this matches your JS fetch call
    path('all_registrations/', views.all_registrations, name='all_registrations'),
    
    # Other urls
    path('categories/', views.CategoriesView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('cart/menu-items/', views.CartView.as_view()),
    path('orders/', views.OrderView.as_view()),
    path('orders/<int:pk>/', views.SingleOrderView.as_view()),
    path('groups/manager/users/', views.GroupViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),

    path('groups/delivery-crew/users/', views.DeliveryCrewViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),

    # Other URL patterns
    path('booking/', views.BookingListView.as_view(), name='booking_list'),
    # Or if you want to add details
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail'),

    path('registering/', views.RegisteringListCreateView.as_view(), name='register_list_create'),
    path('registering/<int:pk>/', RegisteringDetailView.as_view(), name='register_detail'),
  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


# Add code to create Register model
# Create your models here.

class Registering(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Unique username for the user
    email = models.EmailField(max_length=254, unique=True)    # Unique email address for the user
    password = models.CharField(max_length=128)                # Password field (consider using hashed passwords)
    first_name = models.CharField(max_length=30, blank=True)   # Optional first name
    last_name = models.CharField(max_length=30, blank=True)    # Optional last name
    date_joined = models.DateTimeField(auto_now_add=True)        # Automatically set to the current date and time when a user is created




# Add code to create Booking model
# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name



# Add code to create Menu model
# Create your models here.
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 
   image = models.ImageField(upload_to='menu_items/', blank=True, null=True)

   def __str__(self):
      return self.name
  
  
# Add code to create Category model
# Create your models here. 

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)
    

# Add code to create Menu Item model
# Create your models here. 

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    

# Add code to create Cart model
# Create your models here. 

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('menuitem', 'user')
        

# Add code to create Order model
# Create your models here. 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    status = models.BooleanField(default=0, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField(db_index=True)
    


# Add code to create Order Item model
# Create your models here. 

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menuitem')
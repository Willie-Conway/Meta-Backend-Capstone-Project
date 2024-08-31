from django.forms import ModelForm
from .models import Booking, Registering




# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

# Code added for loading form data on the Registration page
class RegestrationForm(ModelForm):
    class Meta:
        model = Registering
        fields = "__all__"
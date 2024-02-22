from django.contrib import admin
from .models import Tour, Category, Review, Reservation

# Register your models here.
admin.site.register(Tour)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Reservation)
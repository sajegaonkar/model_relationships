from django.contrib import admin

# Register your models here.

from .models import Place,Restaurant,Waiter

admin.register(Place)

admin.register(Restaurant)

admin.register(Waiter)
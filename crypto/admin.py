from django.contrib import admin

# Register your models here.
from .models import Currency, Price

admin.site.register(Currency)
admin.site.register(Price)

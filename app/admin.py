from django.contrib import admin
from app.models import Product, Restaurant, Restaurant2, Place


admin.site.register([Place, Restaurant, Restaurant2, Product])


from django.contrib import admin
from payment.models import OrderDetail, Product

admin.site.register([Product, OrderDetail])

from django.contrib import admin
from app.models import Restaurant, Restaurant2, Place


admin.site.register([Place, Restaurant, Restaurant2])

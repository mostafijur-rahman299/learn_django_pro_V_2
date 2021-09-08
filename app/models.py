from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
import datetime


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class Place2(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    class Meta:
        abstract = True


class Restaurant2(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    balance = MoneyField(
            max_digits=14, 
            decimal_places=2, 
            default_currency='USD', 
            null=True, 
            blank=True, 
            validators=[
                MinMoneyValidator(10),
                MaxMoneyValidator(1500),
                MinMoneyValidator(Money(500, 'BDT')),
                MaxMoneyValidator(Money(900, 'NOK')),
                MinMoneyValidator({'EUR': 100, 'USD': 50}),
                MaxMoneyValidator({'EUR': 1000, 'USD': 500}),
            ]
        )
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.description,
            'price': self.price,
            'date_created': self.date_created,
            'date_modified': self.date_modified
        }

from django.db import models
from django.core import validators


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    price = models.FloatField(
        verbose_name='Price',
        validators=[
            validators.MinValueValidator(50),
            validators.MaxValueValidator(100000)
        ],
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.name


class OrderDetail(models.Model):
    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(verbose_name='Customer Email')
    product = models.ForeignKey(to=Product, verbose_name='Product', on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField( max_length=200)
    # This field can be changed as status
    has_paid = models.BooleanField(default=False,verbose_name='Payment Status')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

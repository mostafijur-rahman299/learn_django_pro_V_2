from django.shortcuts import render
from django.conf import settings
import json
import urllib
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.models import Product

from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

 
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def home(request):
    if request.method == 'POST':

        # recaptcha_response = request.POST.get('g-recaptcha-response')

        # url = 'https://www.google.com/recaptcha/api/siteverify'
        # values = {
        #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        #     'response': recaptcha_response
        # }
        # data = urllib.parse.urlencode(values).encode()
        # req = urllib.request.Request(url, data=data)
        # response = urllib.request.urlopen(req)
        # result = json.loads(response.read().decode())

        # if result['success']:
        #     print('yes')

        """Begin hCaptcha validation."""
        hcaptcha_response = request.POST.get('h-captcha-response')

        data = {
            'secret': settings.HCAPTCHA_SECRET_KEY,
            'response': hcaptcha_response
        }
        r = requests.post(settings.VERIFY_URL, data=data)
        result = r.json()

        print(result)

    return render(request, 'index.html', {})
 
 
@api_view(['GET'])
def view_books(request):
 
    products = Product.objects.all()
    results = [product.to_json() for product in products]

    print('books')
    return Response(results, status=status.HTTP_201_CREATED)
 
@api_view(['GET'])
def view_cached_books(request):
    if 'product' in cache:
        # get results from cache
        products = cache.get('product')
        return Response(products, status=status.HTTP_201_CREATED)
 
    else:
        print('init called')
        products = Product.objects.all()
        results = [product.to_json() for product in products]
        # store data in cache
        cache.set('product', results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_201_CREATED)
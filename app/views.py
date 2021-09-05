from django.shortcuts import render
from django.conf import settings
import json
import urllib
import requests


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

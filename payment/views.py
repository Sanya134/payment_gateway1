from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
import requests


class InitiatePaymentView(View):
    def get(self, request):
        return render(request, 'payment/initiate_payment.html')

    def post(self, request, *args, **kwargs):
        headers = {
            "Authorization": "Key 5a7259afe3264285bc0bb3da604ef93d"
        }
        data = {
            "amount": 1000,  # amount in paisa
            "purchase_order_id": "test12",
            "purchase_order_name": "test",
            "return_url": "https://www.yourwebsite.com/buy",
            "website_url": "https://www.yourwebsite.com/",
        }
        
        # return "asd"
        response = requests.post("https://a.khalti.com/api/v2/epayment/initiate/", data=data,
                                 headers=headers)
        response_json = response.json()
        return JsonResponse(response_json)

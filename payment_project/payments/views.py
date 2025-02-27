from django.shortcuts import render

import stripe
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views import View
from .models import Item

class HomePage(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, "home.html", {"items": items})


class CreatePaymentIntent(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        stripe.api_key = settings.STRIPE_KEYS[item.currency]['secret']

        payment_intent = stripe.PaymentIntent.create(
            amount=item.price,
            currency=item.currency,
        )

        return JsonResponse({"client_secret": payment_intent.client_secret})


class ItemDetail(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        stripe_public_key = settings.STRIPE_KEYS[item.currency]['public']

        return render(request, "item_detail.html", {"item": item, "stripe_public_key": stripe_public_key})

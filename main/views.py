import os

import stripe
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv

from .models import Item

load_dotenv()

stripe.api_key = os.getenv('SEC_KEY')


class CreateCheckoutSessionView(View):
    """
    Gets the ID of the Stripe session used for payment for the item chosen.
    Invokes the Stripe checkout session by sending data related to the item.
    """
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        DOMAIN = r'http://127.0.0.1:8000'
        # DOMAIN = r'http://cdcollectionsale.site'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'item_id': item.id
            },
            mode='payment',
            success_url=DOMAIN + '/thanks/',
            cancel_url=DOMAIN + '/index/'
        )
        return JsonResponse({
            'id': checkout_session.id
        })


def item_details(request, pk):
    """
    Displays an individual instance of the model Item.
    """
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
        'STRIPE_PUBLIC_KEY': os.getenv('PUB_KEY')
    }
    return render(request, 'main/item_details.html', context)


def index(request):
    """
    Displays a list of the model Item instances.
    """
    items = Item.objects.all()
    return render(request, 'main/items_list.html', {'items': items})


def thanks(request):
    """
    Displays text after successful payment.
    """
    return render(request, 'main/thanks.html')

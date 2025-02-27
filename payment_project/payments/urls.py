from django.urls import path
from .views import CreatePaymentIntent, ItemDetail, HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('buy/<int:item_id>/', CreatePaymentIntent.as_view(), name='create-payment-intent'),
    path('item/<int:item_id>/', ItemDetail.as_view(), name='item-detail'),
]

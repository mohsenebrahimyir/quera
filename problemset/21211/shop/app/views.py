# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/21211/ ###

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Order


def checkout(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    items = order.orderitem_set.all()
    prices = 0
    for item in items:
        price, count = item.product.price, item.quantity
        prices += price * count

    return JsonResponse({"total_price": prices})

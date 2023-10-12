from django.shortcuts import render

from shop_app.models import Client, Order, OrderItem


def client(request, client_id: int):
    client = Client.objects.get(pk=client_id)
    orders = Order.objects.filter(client=client)
    order_items = {}
    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order_items[order.pk] = []
        for item in items:
            order_items[order.pk].append(item)
    context = {
        'client': client,
        'orders': orders,
        'order_items': order_items,
        'title': f'Orders by {client.str_to_title()}'
    }
    return render(request, "shop_app/client.html", context)

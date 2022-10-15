from django.shortcuts import render
from django.http import JsonResponse
from .models import CartItem


def index(request):
    return render(request, 'cart/index.html', {
        'title': 'Перегляд кошика',
        'user_cart_items': CartItem.objects.filter(user_id=request.user.id)
    })


def ajax_cart(request):
    response = dict()

    # 1 -Отримуємо значення get параметрів із AJAX запиту:
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')

    # 2 - зберігаю товар доданий до кошика у БД
    CartItem.objects.create(
        user_id=uid,
        product_id=pid,
        status='Очікування замовлення'
    )

    response['message'] = 'Товар збережений'

    # 3 - Зчитуємо із бази список всіх товарів даного користувача
    user_items = CartItem.objects.filter(user_id=uid)

    # 4 - обчислюємо загальну вартість всіх твоарів даного користувача
    amount = 0
    # amount = list(filter(lambda p: p.product.price, user_items))
    for item in user_items:
        amount += item.product.price

    # 5 - Записуємо у відповідь сервера загальну кількість та вартість товарів
    response['count'] = len(user_items)
    response['amount'] = amount

    return JsonResponse(response)


def ajax_cart_display(request):
    response = dict()

    # 1 -Отримуємо значення get параметрів із AJAX запиту:
    uid = request.GET.get('uid')

    # 2 - Зчитуємо із бази список всіх товарів даного користувача
    user_items = CartItem.objects.filter(user_id=uid)

    # 3 - обчислюємо загальну вартість всіх твоарів даного користувача
    amount = 0
    # amount = list(filter(lambda p: p.product.price, user_items))
    for item in user_items:
        amount += item.product.price

    # 4 - Записуємо у відповідь сервера загальну кількість та вартість товарів
    response['count'] = len(user_items)
    response['amount'] = amount

    return JsonResponse(response)


def ajax_del_item(request):
    item_id = request.GET['item_id']
    del_item = CartItem.objects.get(id=item_id)
    del_item.delete()
    return JsonResponse({
        'message': f'Товар із ID: {item_id} був видалений із кошика!'
    })

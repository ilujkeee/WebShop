from django.shortcuts import render
from cart.models import CartItem
from django.core.mail import send_mail


def bill(request, sel_list: str):
    sel_list_str_array = sel_list.split(',')
    sel_list_num_array = [int(x) for x in sel_list_str_array[:-1]]
    total_price = int(sel_list_str_array[-1])
    final_list = []

    for item_id in sel_list_num_array:
        item = CartItem.objects.get(id=item_id)
        final_list.append({
            'product_name': item.product.name,
            'category_name': item.product.category.name,
            'product_price': item.product.price,
            'product_photo': item.product.photo
        })

    return render(request, 'orders/bill.html', {
        'title': 'Оформлення рахунку',
        'total_price': total_price,
        'final_list': final_list,
        'init_list': sel_list
    })


def confirm(request, init_list: str):
    if request.method == 'GET':
        return render(request, 'orders/confirm.html', {
            'title': 'Підтверження замовлення',
            'init_list': init_list
        })
    elif request.method == 'POST':
        email = request.POST['email']
        sel_list_str_array = init_list.split(',')
        sel_list_num_array = [int(x) for x in sel_list_str_array[:-1]]
        total_price = int(sel_list_str_array[-1])
        info_list = []
        #
        for item_id in sel_list_num_array:
            cart_item = CartItem.objects.get(id=item_id)
            info_list.append({
                'product_name': cart_item.product.name,
                'category_name': cart_item.product.category.name,
                'product_price': cart_item.product.price
            })
        #
        subject = 'Повідомлення про замовлення на сайті WebShop'
        body = """
            <h1>Повідомлення про замовлення на сайті WebShop</h1>
            <hr />
            <h2 style="color: purple">Ви підтвердили замовлення наступних товарів:</h2>
            <h3>
            <ol>
        """
        #
        for info in info_list:
            body += f"""
                <li>{info.get('product_name')} / {info.get('category_name')} - {info.get('product_name')}.00 грн.</li>
            """
        body += f"""
            </ol>
            </h3>
            <h2>Загальна сума до сплати: <span style="color: red">{total_price}.00 грн.</span>
        """
        #
        success = send_mail(subject, '', 'WebShop', [email], fail_silently=False, html_message=body)
        if success:
            return render(request, 'orders/thanks.html', {
                'title': 'Подяка за замовлення',
                'email': email
            })
        else:
            return render(request, 'orders/faild.html', {
                'title': 'Помилка поштового відправлення'
            })


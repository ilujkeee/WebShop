$(document).ready(() => {

    console.log('cart-script -> start');

    $('#products').on('click', '.add-to-cart-btn', (event) => {
        console.log('addToCart -> click');
        //
        const userId = $('#user_id').val();
        console.log('userId' + userId);
        //
        if (userId === 'None') {
            alert('Для використання кошика Ви маєте авторизуватись!');
            //window.location = '/accounts/sing_in'; //-temp: page create
        } else {
            let productId = $(event.target).prev().val();
            let productName = $(event.target).parent().prev().find('h3').text();
            let productPrice = $(event.target).parent().prev().find('h4').text();

            productPrice = parseFloat(productPrice)

            console.log('productId -> ' + productId);
            console.log('productName -> ' + productName);
            console.log('productPrice -> ' + productPrice);

            //AJAX-запит на збереження товару, доданого в кошик користувача, у БД
            $.ajax({
                url: '/cart/ajax_cart',
                data: `uid=${userId}&pid=${productId}`,
                success: (response) => {
                    console.log(response.message);
                    $('#cart_count').text(response.count);
                    $('.cart-summary').find('h5').text(response.count + ' товарів обрано');
                    $('.cart-summary').find('h4').text('ВАРТІСТЬ: ' + response.amount + 'грн.');

                }
            })

        }
    });

})

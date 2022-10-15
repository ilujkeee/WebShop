$(document).ready(() => {

    console.log('cart_display -> start');

    const userId = $('#user_id').val();

    $.ajax({
        url: '/cart/ajax_cart_display',
        data: `uid=${userId}`,
        success: (response) => {
            console.log(response.message);
            $('#cart_count').text(response.count);
            $('.cart-summary').find('h5').text(response.count + ' товарів обрано');
            $('.cart-summary').find('h4').text('ВАРТІСТЬ: ' + response.amount + 'грн.');
        }

    });

});
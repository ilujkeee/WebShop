$(document).ready(() => {
    console.log('del_cart_item -> start');

    $('.del-btn').click((event) => {
        let itemId = $(event.target).prev().val();
        console.log('del-btn -> click / itemId = ' + itemId);
        $.ajax({
            url: '/cart/ajax_del_item',
            data: 'item_id=' + itemId,
            success: (response) => {
                console.log(response.message);
                alert(response.message);
                window.location = '/cart';
            }
        })
    });

})
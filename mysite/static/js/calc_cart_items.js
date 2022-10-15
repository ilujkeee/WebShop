const doCalculate = () => {
    //1
    let checkedCells = $('.check:checked');
    let totalPrice = 0;
    let selItemsList = '';

    //2
    for (let cell of checkedCells) {
        let parent = $(cell).parent().parent();   //tr with check-cell!
        totalPrice += parseFloat($(parent).find('td.price_cell').text());
        selItemsList += $(parent).find('td.id_cell').text() + ',';
    }
    selItemsList += totalPrice;

    //3
    console.log('totalPrice = ' + totalPrice);
    console.log('selItemsList = ' + selItemsList);
    $('#total').text(totalPrice.toFixed(2) + ' грн.');
    $('#bill-btn').attr('href', '/orders/bill/' + selItemsList);
};


$(document).ready(() => {
   //1
    console.log('calc_cart_items -> start');
    doCalculate();

    //2
    $('.check').click(() => {
        console.log('.check -> click');
        doCalculate();
    })
});
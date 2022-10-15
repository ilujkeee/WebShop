$(document).ready(() => {

    console.log('category_select -> start');

    $('.input-checkbox > input').click((event) => {
        console.log('category-checkbox -> click');
        let status = $(event.target).is(':checked');
        console.log('category-status -> ' + status)
        let cname = $(event.target).attr('id');
        console.log('category-name -> ' + cname);


    });
});
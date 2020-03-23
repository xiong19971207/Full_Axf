$(function () {
    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');
        $('#all_type_container').toggle();
    });

        $('#sort_rule').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');
        $('#all_sort_rule').toggle();
        });

        $('.addShopping').click(function () {
           var $button = $(this);

           var goodsid = $button.attr('goodsid');
           $.get('/cart/addtoCart/',
               {'goodsid':goodsid},
               function (data) {
                   if(data['status'] === 200){
                        //button标签的上一个标签
                        $button.prev().html(data['c_goods_num']);
                   }else{
                       window.location.href = '/user/login/'
                   }
               })

        })

    });
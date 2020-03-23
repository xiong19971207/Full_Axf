from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from CartApp.models import AxfCart
from CartApp.views import get_total_price
from OrderApp.models import AxfOrder, AxfOrderGoods
from axf002.settings import app_private_key_string, alipay_public_key_string


def order_detail(request):
    order_id = request.GET.get('order_id')

    order = AxfOrder.objects.get(pk=order_id)

    context = {
        'order':order,
        'total_price':order.axfordergoods_set.first().og_total_price
    }

    return render(request,'axf/order/order_detail.html',context=context)


def make_order(request):

    # 创建order对象--->为了ordergoods
    user_id = request.session.get('user_id')

    order = AxfOrder()

    order.o_user_id = user_id

    order.save()

    # 将购物车中选中的数据 交给ordergoods的og_goods

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)

    for cart in carts:
        # 创建ordergoods对象
        orderGoods = AxfOrderGoods()

        orderGoods.og_order = order

        orderGoods.og_goods = cart.c_goods

        orderGoods.og_total_price = get_total_price(user_id)

        # og_price就是商品的数量
        orderGoods.og_goods_num = cart.c_goods_num

        orderGoods.save()

        cart.delete()

    data = {
        'msg': 'ok',
        'status': 200,
        'order_id': order.id
    }

    return JsonResponse(data=data)


def alipay(request):
    alipay = AliPay(
        appid="2016101200665774",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA",  # RSA 或者 RSA2
    debug = False  # 默认False
    )

    subject = "兰波激励"

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="20161112",
        total_amount=10,
        subject=subject,
        return_url="https://www.1000phone.com",
        notify_url="https://www.1000phone.com"  # 可选, 不填则使用默认notify url
    )
    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)
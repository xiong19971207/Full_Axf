from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import AxfCart


def cart(request):
    user_id = request.session.get('user_id')
    if user_id:

        carts = AxfCart.objects.filter(c_user_id=user_id)

        #选中的，，同一个购物车
        is_all_select = not AxfCart.objects.filter(c_is_select=False).filter(c_user_id=user_id).exists()

        context = {
            'carts':carts,
            'total_price':get_total_price(user_id),
            'is_all_select':is_all_select
        }

        return render(request, 'axf/main/cart/cart.html',context=context)
    else:
        return render(request, 'axf/user/login.html')

def get_total_price(user_id):

    carts = AxfCart.objects.filter(c_user_id = user_id).filter(c_is_select = True)

    total_prise = 0

    for cart in carts:
        total_prise = total_prise + cart.c_goods_num*float(cart.c_goods.price)

    return '%.2f'%total_prise

def addtoCrat(request):
    #session查询，查询是否登陆
    user_id = request.session.get('user_id')

    data = {
        'msg': 'ok',
        'status': 200
    }

    if user_id:
        goodsid = request.GET.get('goodsid')

        #联合主键查询
        carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goodsid)

        if carts.count() > 0:
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = AxfCart()
            cart.c_goods_id = goodsid
            cart.c_user_id = user_id


        cart.save()

        data['c_goods_num'] = cart.c_goods_num

        return JsonResponse(data=data)

    else:
        data['msg']='未登录'
        data['status'] = 201
        return JsonResponse(data=data)


@csrf_exempt
def subCart(request):

    user_id = request.session.get('user_id')

    data = {
        'msg':'ok',
        'status':200,
        # 'total_price':get_total_price(user_id)
    }

    cartid = request.POST.get('cartid')
    print(cartid)

    cart = AxfCart.objects.get(pk = cartid)
    if cart.c_goods_num > 1:
        cart.c_goods_num = cart.c_goods_num - 1
        cart.save()
        data['c_goods_num'] = cart.c_goods_num
    else:
        cart.delete()
        data['status'] = 204

    data['total_price'] = get_total_price(user_id)

    return JsonResponse(data=data)


def changeStatus(request):

    data = {
        'msg':'ok',
        'status':200
    }

    cartid = request.GET.get('cartid')

    print('================')
    print(cartid)

    cart = AxfCart.objects.get(pk=cartid)
    print(cart)

    cart.c_is_select = not cart.c_is_select

    cart.save()
    data['c_is_select'] = cart.c_is_select

    user_id = request.session.get('user_id')
    data['total_price'] = get_total_price(user_id)

    #所有非未选中的
    is_all_select = not AxfCart.objects.filter(c_is_select=False).exists()

    data['is_all_select'] = is_all_select

    return JsonResponse(data=data)


def allSelect(request):
    cartidlist = request.GET.get('cartidlist')

    cartid_list = cartidlist.split('#')

    carts = AxfCart.objects.filter(id__in=cartid_list)

    user_id = request.session.get('user_id')


    data = {
        'msg': 'ok',
        'status': 200,
    }

    for cart in carts:
        cart.c_is_select = not cart.c_is_select
        cart.save()

    data['total_price'] = get_total_price(user_id)

    return JsonResponse(data=data)
from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods


def market(request):
    typeid = request.GET.get('typeid','104749')

    axffoodtypes = AxfFoodType.objects.all()

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames

    child_type = childtypenames.split('#')

    # type_name = child_type.split(':')[0]
    type_name_list = []

    for child_name in child_type:
        type_name = child_name.split(':')
        type_name_list.append(type_name)

    axfgoods = AxfGoods.objects.filter(categoryid=typeid)

    childcid = request.GET.get('childcid','0')

    if childcid == '0':
        pass
    else:
        axfgoods = axfgoods.filter(childcid=childcid)



    sort_rule = [
          ['综合排序','0'],
          ['价格升序','1'],
          ['价格降序','2'],
          ['销量升序','3'],
          ['销量降序','4'],
    ]

    sortrule = request.GET.get('sortrule','0')

    if  sortrule =='0':
        pass
    elif sortrule == '1':
        axfgoods = axfgoods.order_by('price')
    elif sortrule == '2':
        axfgoods = axfgoods.order_by('-price')
    elif sortrule == '3':
        axfgoods = axfgoods.order_by('productnum')
    elif sortrule == '4':
        axfgoods = axfgoods.order_by('-productnum')

    context = {
        'axffoodtypes': axffoodtypes,
        'axfgoods':axfgoods,
        'typeid':typeid,
        'type_name_list':type_name_list,
        'childcid':childcid,
        'sort_rule':sort_rule,
        'sortrule':sortrule,
    }

    return render(request, 'axf/main/market/market.html', context=context)



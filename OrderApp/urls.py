from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    url(r'^order_detail/',views.order_detail,name='order_detail'),

    url(r'^make_order/',views.make_order,name='make_order'),

    url(r'^testalipay/',views.alipay,name='alipay'),
]
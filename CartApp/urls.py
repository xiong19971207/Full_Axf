from django.conf.urls import url

from CartApp import views

urlpatterns = [
    url(r'^cart/',views.cart,name='cart'),
    url(r'^addtoCart/', views.addtoCrat,name='addtoCart'),

    url(r'^subCart/', views.subCart, name='subCart'),
    url(r'^changeStatus/',views.changeStatus,name='changeStatus'),

    url(r'^allSelect/',views.allSelect,name='allSelect')

]
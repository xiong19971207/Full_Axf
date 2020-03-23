from django.conf.urls import url

from HomeApp import views

urlpatterns = [
    url(r'^index/',views.index),
    url(r'^home/',views.home,name='home')
]
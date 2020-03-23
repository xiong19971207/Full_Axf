from django.db import models

# Create your models here.
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


class AxfCart(models.Model):
    #关系表中的外键是唯一的
    c_goods = models.ForeignKey(AxfGoods)
    c_user = models.ForeignKey(AxfUser)

    #默认的商品数量
    c_goods_num = models.IntegerField(default=1)
    c_is_select = models.BooleanField(default=True)

    class Meta:
        db_table='cart'
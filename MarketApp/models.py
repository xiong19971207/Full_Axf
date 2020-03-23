from django.db import models

# Create your models here.
# typeid,typename,childtypenames,typesort
class AxfFoodType(models.Model):
    typeid = models.CharField(max_length=256)
    typename = models.CharField(max_length=256)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtype'



class AxfGoods(models.Model):
        # 商品id
        productid = models.CharField(max_length=10)
        # 商品图片
        productimg = models.CharField(max_length=150)
        # 商品名称
        productname = models.CharField(max_length=50)
        # 商品长名称
        productlongname = models.CharField(max_length=100)
        # 是否精选
        isxf = models.NullBooleanField(default=False)
        # 是否买一赠一
        pmdesc = models.CharField(max_length=10)
        # 规格
        specifics = models.CharField(max_length=20)
        # 价格
        price = models.CharField(max_length=10)
        # 超市价格
        marketprice = models.CharField(max_length=10)
        # 组id
        categoryid = models.CharField(max_length=10)
        # 子类组id
        childcid = models.CharField(max_length=10)
        # 子类组名称
        childcidname = models.CharField(max_length=10)
        # 详情页id
        dealerid = models.CharField(max_length=10)
        # 库存
        storenums = models.IntegerField()
        # 销量
        productnum = models.IntegerField()
        class Meta:
            db_table='axf_goods'






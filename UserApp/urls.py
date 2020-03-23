from django.conf.urls import url

from UserApp import views

urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^checkname/',views.checkname,name='checkname'),

    #邮箱检测
    url(r'^testmail/',views.testmail),

    #发送邮件
    url(r'^sendemil/',views.sendemil),

    #激活邮箱
    url(r'^activeAccount/',views.activeAccount),

    #登陆页面
    url(r'^login/',views.login,name='login'),

    #验证码
    url(r'^get_code/',views.get_code),

    #退出登陆
    url(r'^loginout/',views.loginout,name='loginout')
]
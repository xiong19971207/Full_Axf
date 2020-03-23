import re
import uuid

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw


from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.six import BytesIO

from UserApp.models import AxfUser
from UserApp.view_constaint import send_email
from axf002 import settings


def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        #加密密码，怎么破解跟我无关
        password = make_password(password)
        print(password)

        user = AxfUser()

        user.u_name = name
        user.u_password = password
        user.u_email = email
        user.u_icon = icon

        token = uuid.uuid4()
        user.u_token = token


        user.save()

        #设置邮件过期时间，用id匹配token,用别的有泄漏信息的风险
        cache.set(token,user.id,timeout=90)

        send_email(name,email,token)
        return render(request,'axf/user/login.html')


def checkname(request):

    name = request.GET.get('name')

    users = AxfUser.objects.filter(u_name=name)

    data = {
        'msg':'用户名可以使用',
        'status':200,
    }

    if users.count() > 0:
        data['msg']='用户名已经存在'
        data['status'] = 201

    return JsonResponse(data=data)

#测试发送邮件
def testmail(request):
    subject = '红浪漫洗浴'
    message = '来来来，小老弟'
    html_message = '<h1>还已注册</h1>'
    from_email = '17855370672@163.com'
    recipient_list = ['17855370672@163.com']
    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)
    return HttpResponse('666')


def sendemil(request):
    subject = '红浪漫洗浴中心'
    message = '这是没用的东西，但是不能不加'

    context = {
        'name' : '熊',
        'url'  : 'http://www.baidu.com',
    }

    #loader方法要导入
    html_message = loader.get_template('active.html').render(context=context)
    from_email = '17855370672@163.com'
    recipient_list = ['17855370672@163.com']
    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)
    return HttpResponse('邮件已经发送')


def activeAccount(request):

    token = request.GET.get('token')
    # print('123456')
    # user1 = AxfUser.objects.filter(u_token=token)
    #
    # if user1.exists():
    #     user = user1.first()
    #     user.u_active = 1
    #     user.save()
    #     return HttpResponse('激活成功')
    # else:
    #     return HttpResponse('别跟我开玩笑')

    user_id = cache.get(token)

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        user.u_active = True
        user.save()

        #只验证一次，让其不能再次验证成功
        cache.delete(token)

        return HttpResponse('添加成功')
    else:
        return HttpResponse('邮件已过期，请重新发送')


def login(request):
    if request.method == 'GET':
        return render(request,'axf/user/login.html')
    if request.method == 'POST':
        #用户输入的验证码
        imgcode = request.POST.get('imgcode')
        #所有的验证码都会把验证码的值写到session上
        verify_code = request.session.get('verify_code')

        #不区分大小写 search和match没有区别
        b = re.search(imgcode,verify_code,re.IGNORECASE)

        if b:
            name = request.POST.get('name')
            users = AxfUser.objects.filter(u_name=name)
            if users.count() > 0:
                user = users.first()
                password = request.POST.get('password')

                print('============')
                print(password)
                print(user.u_password)

                if check_password(password,user.u_password):

                    if user.u_active == True:

                        request.session['user_id'] = user.id

                        return redirect(reverse('mine:mine'))
                    else:
                        msg = '用户未激活'
                        context = {
                            'msg': msg
                        }
                        return render(request, 'axf/user/login.html', context=context)

                else:
                    msg = '密码错误'
                    context = {
                        'msg': msg
                    }
                    return render(request, 'axf/user/login.html', context=context)


            else:
                msg = '用户不存在'
                context = {
                    'msg':msg
                }
            return render(request,'axf/user/login.html',context=context)

        else:
            msg='验证码不正确'
            return render(request,'axf/user/login.html',context=locals())



def get_code(request):

    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")
import random
def get_color():
    return random.randrange(256)
def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def loginout(request):
    request.session.flush()
    return redirect(reverse('mine:mine'))
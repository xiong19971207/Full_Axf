from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader


def send_email(name,email,token):

    subject = '红浪漫洗浴中心'
    message = '这是没用的东西，但是不能不加'

    context = {
        'name' : name,
        'url'  : "http://127.0.0.1:8000/user/activeAccount?token="+str(token),
    }

    html_message = loader.get_template('active.html').render(context=context)
    from_email = '17855370672@163.com'

    #传入参数后不能瞎写
    recipient_list = [email]

    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)

    #此时可以没有  return
    return HttpResponse('邮件已经发送')
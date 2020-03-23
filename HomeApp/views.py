from django.http import HttpResponse
from django.shortcuts import render
from HomeApp.models import AxfWheel, AxfNav, AxfMustBuy, AxfMainShow


# Create your views here.
def index(request):
    return HttpResponse('index')


def home(request):

    wheels = AxfWheel.objects.all()

    navs = AxfNav.objects.all()

    mustbuys = AxfMustBuy.objects.all()

    mainshows = AxfMainShow.objects.all()

    return render(request,'axf/main/home/home.html',context=locals())
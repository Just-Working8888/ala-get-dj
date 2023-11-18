from django.shortcuts import render
from apps.betaxist.models import Betaxist,EarnMoney
from apps.base.models import Settings, Base


# Create your views here.
def betaxist(request):
    betaxist = Betaxist.objects.latest('id')
    settings = Settings.objects.latest('id')
    earnnoney = EarnMoney.objects.all()
    base = Base.objects.latest('id')

    return render(request, 'beTaxist.html', locals())
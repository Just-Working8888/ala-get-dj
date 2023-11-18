from django.shortcuts import render
from apps.base.models import Settings, Slider, Why, Base, Environment

# Create your views here.
def settings(request):
    settings = Settings.objects.latest('id')
    slider = Slider.objects.all()
    why = Why.objects.all().order_by('?')[:3]
    whys = Why.objects.latest('id')
    base = Base.objects.latest('id')
    environment = Environment.objects.latest('id')


    return render(request, 'index.html', locals())
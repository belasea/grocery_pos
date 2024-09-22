from django.shortcuts import render
from home.models import Slider


# Create your views here.
def home(request):
    return render(request, 'home/home.html')
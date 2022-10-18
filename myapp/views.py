from django.shortcuts import render
from .models import Item


# Create your views here.
def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'products', context)

from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    context = {
        'message': "hola mundo"
    }
    return render(request, 'example/index.html', context)

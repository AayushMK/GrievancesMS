from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def home(request):
    #home_html_page = loader.get_template('../ui/index.html')
    home_html_page = loader.get_template('../ui/index2.html')

    return HttpResponse(home_html_page.render(None, request))

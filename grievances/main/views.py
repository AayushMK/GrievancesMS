from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def main(request):
    #home_html_page = loader.get_template('../ui/index.html')
    main_html_page = loader.get_template('../ui/main.html')
    context = {}
    if "login_user" in request.session:
        context["login_user"] = request.session["login_user"]

    return HttpResponse(main_html_page.render(context, request))

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from utils import timestamp, to_date, generate_uuid
from model.grievance import Grievance
from repo.grievances_repo import GrievanceRepo

# Create your views here.


def post_g(request):
    post_g_html_page = loader.get_template('../ui/grievance_form.html')
    return HttpResponse(post_g_html_page.render(None, request))


def submit(request):
    post_g_html_page = loader.get_template('../ui/grievance_form.html')
    main_html_page = loader.get_template('../ui/main.html')
    context = {}
    if request.method == 'POST':
        title = request.POST["title"]
        body = request.POST["body"]
        g_id = generate_uuid()
        grievance = Grievance()
        grievance.g_id = g_id
        grievance.title = title
        grievance.body = body
        grievance.created_date = timestamp()
        grievance.approvals = 0
        grievance.user = request.session["login_user"]
        grepo = GrievanceRepo()
        result = grepo.saveGrievance(grievance)
        if result == True:
            context["success_msg"] = "Successful to load into database"
        else:
            context["error"] = "Unable to load into database"
        context["time"] = to_date(grievance.created_date)
        context["title"] = grievance.title
        context["body"] = grievance.body
        return redirect("main")

    return HttpResponse(post_g_html_page.render(None, request))

from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from model.user import User
from model.user_register import UserRegister
from service.account_services import AccountService


def signup(request):
    signup_html_page = loader.get_template('../ui/index2.html')
    context = {}
    if request.method == 'POST':
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["pwd"]
        cpassword = request.POST["cpwd"]
        semester = request.POST["sem"]
        regNo = request.POST["regno."]
        user = User()
        user.user_name = username
        user.email = email
        user.semester = semester
        user_register = UserRegister()
        user_register.user = user
        user_register.password = password
        user_register.cpassword = cpassword
        context["user_register"] = user_register
        if not username or len(str(username).strip(' ')) <= 4:
            context["error_msg"] = "Invalid user name. Should be greater than 4."
        elif not email:
            context["error_msg"] = "Invalid email."
        elif not password or len(str(password).strip(' ')) <= 7:
            context["error_msg"] = "Password must be 8 character long."
        elif not cpassword or cpassword != password:
            context["error_msg"] = "Password don't match."
        else:
            account_service = AccountService()
            service_response = account_service.signup(user_register)
            if service_response is None:
                context["error_msg"] = "Could not save user."
            else:
                context["success_msg"] = "User saved successfully."

    return HttpResponse(signup_html_page.render(context, request))


def signin(request):
    signin_html_page = loader.get_template('../ui/index2.html')

    context = {}
    if request.method == 'POST':
        email = request.POST["semail"]
        password = request.POST["spwd"]
        if not email:
            context["error_msg"] = "Invalid email or password."
        else:
            account_service = AccountService()
            user = account_service.signin(email, password)
            if user is None:
                context["error_msg"] = "Invalid email or password database."

            else:
                request.session["login_user"] = user
                context["success_msg"] = "Login successful."
                return redirect("main")

    return HttpResponse(signin_html_page.render(context, request))


def signout(request):
    request.session.flush()
    return redirect("home")

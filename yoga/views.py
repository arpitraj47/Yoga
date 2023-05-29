from django.http import JsonResponse
from django.shortcuts import render

from yoga.models import user_information


# Create your views here.

def index(request):
    return render(request, "index.html")

def registration_form(request):
    return render(request, "registration_form.html")

# def login_form(request):
#     return login_form(request, "login_form")

def user_registration(request):
    name = request.POST.get('username')
    email = request.POST.get('email')
    age = request.POST.get('age')
    password = request.POST.get('password')

    data1 = user_information.objects.filter(email=email)
    if len(data1)!=0:
        return JsonResponse({"Massage":"You are already registered"})

    query = user_information(user_name=name, email=email, age=age, password=password)
    query.save()

    return JsonResponse({"massage": "Registration Successfully"})


def  login_form(request):
    return render(request, 'login_form.html')

def user_login(request):
    email = request.POST.get("mail")
    password = request.POST.get("Password")
    data = user_information.objects.filter(email=email)
    if len(data)==0:
        JsonResponse({"massage": "Enter correct email"})
    else:
        data1 = user_information.objects.filter(email=email).values()
        d=data1[0]
        print(d['password'])
        if str(d['password']) == password:
            return render(request, 'home.html', {"Massage": "Login Successfully"})
        else:
            return JsonResponse({"Massage": "Incorrect Password"})





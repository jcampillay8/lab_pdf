# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'index.html')

def users(request):
    context = {
        'user_list': User.objects.all()
    }
    return render(request, "users.html", context)


def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')

def register(request):
    errors = User.objects.register_validator(request.POST)
    
    if(len(errors)):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('home')
    else:
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        num_pag = request.POST.get('num_pa')
        domic = request.POST.get('domic')
        num_op = request.POST.get('num_op')
        fecha_suscr = request.POST.get('fecha_suscr')
        monto_i = request.POST.get('monto_i')
        User.objects.create(first_name=firstName, last_name=lastName, domic=domic, num_pa=num_pag, num_op=num_op, fecha_suscr=fecha_suscr, monto_i=monto_i)
        user = User.objects.last()
        return redirect ('success', id=user.id)

def success(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, "success.html", context)

def login(request):
    if request.method == "POST":

        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")

        user = User.objects.get(email=request.POST['loginEmail'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            print("User Password Matches")
            request.session["id"]=user.id
            request.session["first_name"]=user.first_name
            return redirect("/tvshow/tvshow")
        else:
            print("User Password Match Fails")
            return redirect("/")
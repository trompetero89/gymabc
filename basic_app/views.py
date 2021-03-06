from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm,PaymentsForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from . import models

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("iniciaste sesión")



@login_required
def user_logout(request):
    logout(request)
    return  HttpResponseRedirect(reverse('index'))




@login_required
def payments(request):
    payments_form = PaymentsForm()
    return render(request,'basic_app/payments.html',{'payments_form':payments_form})




def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})


def user_login(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Cuenta no activa")
        else:
            print("alguién intentó iniciar sesión de manera fallida")
            print("Nombre de usuario:{} y password {}".format(username,password))
            return HttpResponse("datos inválidos")

    else:
        return render(request,'basic_app/login.html',{})



class MenuListView(ListView):
    context_object_name = 'menus'
    model = models.Menu

class MenuDetailView(DetailView):
    context_object_name = 'menu_detail'
    model = models.Menu
    template_name = 'basic_app/menu_detail.html'


class MenuCreateView(CreateView):
    fields = ('name','provider','location')
    model = models.Menu

class MenuUpdateView(UpdateView):
    fields = ('name','provider')
    model = models.Menu
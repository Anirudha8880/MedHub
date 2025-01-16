from django.contrib.messages.context_processors import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_view(request):
    if request.method=="POST":
        un = request.POST.get("username")
        ps = request.POST.get("password")
        user = authenticate(request,username=un,password=ps)
        if user is not None:
            login(request, user)
            return redirect("/medhub/home/")
        else:
            messages.error(request,'Invalid Username/Password')
    template_name='AuthApp/login.html'
    context={}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('/auth/login/')

def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth/login/')
    template_name="AuthApp/register.html"
    context={'form':form}
    return render(request, template_name, context)
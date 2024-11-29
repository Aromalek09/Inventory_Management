from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView,CreateView
from .form import *
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.



class LoginView(FormView):
    template_name='login.html'
    form_class=LoginForm
    
    def post(self,request):
        form=LoginForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pswd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Login Failed")
                return redirect('log')
        return render(request,"login.html",{"form":form})
    


class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy('log')
    
class logoutview(View):
    def get(Self,request):
        logout(request)
        return redirect('log')
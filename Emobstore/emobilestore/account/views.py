from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,View
from .models import CustUser
from django.urls import reverse_lazy
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.


class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user:
                if user.usertype=="Customer":
                    login(request,user)
                    return redirect("custh")
                elif user.usertype=="Store":
                    login(request,user)
                    return redirect("storeh")
            else:
                return redirect("log")
        


class RegView(CreateView):
    model=CustUser
    template_name="reg.html"
    success_url=reverse_lazy("log")
    form_class=RegForm
    def form_valid(self,request):
        messages.success(self.request,"registration succesfull")
        return redirect('log')

class LogOutView(View):
    def get(self,request):
        logout(request)
        return redirect("log")
from django.shortcuts import render,redirect
from django.views.generic import FormView,DeleteView,UpdateView,View,TemplateView,CreateView
from .forms import CPassForm
from django.contrib.auth import authenticate,logout
from .forms import AddProductForm
from account.models import products
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("log")
    return wrapper


@method_decorator(signin_required,name='dispatch')
class StoreHome(TemplateView):
    template_name="storehome.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=products.objects.filter(user=self.request.user)
        return context

@method_decorator(signin_required,name='dispatch')
class AddProduct(CreateView):
    template_name="addprod.html"
    form_class=AddProductForm
    model=products
    success_url=reverse_lazy("storeh")
    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"product added")
        self.object=form.save()
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=products.objects.all()
        return context
    

@method_decorator(signin_required,name='dispatch')
class Productview(TemplateView):
    template_name="viewprod.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=products.objects.filter(user=self.request.user)
        return context

@method_decorator(signin_required,name='dispatch')
class Edit(UpdateView):
    model=products
    template_name="edit.html"
    form_class=AddProductForm
    success_url=reverse_lazy("vpro")
    pk_url_kwarg="pk"
    def form_valid(self,form):
        messages.success(self.request,"Product Updated succesfully")
        self.object=form.save()
        return super().form_valid(form)    

@method_decorator(signin_required,name='dispatch')
class Deletep(DeleteView):
    model=products
    template_name='delete.html'
    success_url=reverse_lazy("vpro")

@method_decorator(signin_required,name='dispatch')
class MyProductView(TemplateView):
    template_name="viewprod.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=products.objects.filter(user=self.request.user)
        return context
    
class CPassView(FormView):
    template_name="changepass.html"
    form_class=CPassForm
    def post(self,request,*args,**kwargs):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            old=form.cleaned_data.get("old_pass")
            new=form.cleaned_data.get("new_pass")
            cnf=form.cleaned_data.get("confirm_pass")
            user=authenticate(request,username=request.user.username,password=old)
            if user:
                if new==cnf:
                    # user.password=new
                    # user.save()
                    user.set_password(new)
                    user.save()
                    logout(request)
                    messages.success(request,"Password Changed")
                    return redirect("log")
                else:
                    messages.error(request,"Password Mismatch")
                    return redirect("cpass")
            else:
                messages.error(request,"Password incorect")
                return redirect("cpass")



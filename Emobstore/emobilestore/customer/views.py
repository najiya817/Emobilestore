from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,DeleteView
from .models import CartItem,OrderItem
from .forms import OrderForm
from account.models import products
from store.forms import AddProductForm
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect


# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect("log")
    return wrapper


@method_decorator(signin_required,name='dispatch')
class CustHome(CreateView):
    template_name="custhome.html"
    model=products
    form_class=AddProductForm
    def get(self,request,*args,**kwargs):
        data=products.objects.all()
        return render(request,"custhome.html",{"data":data}) 



    





class ViewCart(TemplateView):
    template_name="addtocart.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['data']=CartItem.objects.filter(user=self.request.user)
        return context

# class ViewCart(View):
#     def get(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             pro=CartItem.objects.all()
#             return render(request,"addtocart.html",{"data":pro})
#         else:
#             return redirect('custh')
#         print('data')

# class DeleteCart(DeleteView):
#     model=CartItem
#     success_url=reverse_lazy("tocart")
#     def delete(self, **kwargs):
#         id=kwargs.get("pk")
#         context=super().get_context_data(**kwargs)
#         context['pro']=CartItem.objects.get(id=self.kwargs.get("id"))
#         return context

class DeleteCart(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("id")
        pr=CartItem.objects.get(id=pid)
        pr.delete()
        return redirect('vcart')

class OrderItem(CreateView):
    model=products
    form_class=OrderForm
    template_name='orderitem.html'
    success_url=reverse_lazy('products')


class CheckOutView(TemplateView):
    template_name="checkout.html"








def add_to_cart(request,id):
    user = request.user
    product = products.objects.get(id=id)
    # when user is authenticated
    if user.is_authenticated:

            try:
                cart_item = CartItem.objects.get(product=product,user=user)
                cart_item.quantity += 1
                cart_item.save()
            except CartItem.DoesNotExist:
                cart_item = CartItem.objects.create(
                    product=product,
                    user=user,
                    quantity = 1,
                )
                cart_item.save()
            
            return redirect('custh')
    
    
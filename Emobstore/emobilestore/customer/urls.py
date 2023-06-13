from django.urls import path
from .views import CustHome,ViewCart,DeleteCart,OrderItem,CheckOutView,add_to_cart

urlpatterns = [
    path('cust/',CustHome.as_view(),name="custh"),
    path('vc/',ViewCart.as_view(),name='vcart'),
    path('delc/<int:id>',DeleteCart.as_view(),name='delcrt'),
    path('ord/',OrderItem.as_view(),name='orderi'),
    path('ch/',CheckOutView.as_view(),name='chk'),
    path('crt/<int:id>',add_to_cart,name='cart')
]
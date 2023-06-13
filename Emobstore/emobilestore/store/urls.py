from django.urls import path
from .views import StoreHome,AddProduct,Edit,Deletep,MyProductView,Productview,CPassView


urlpatterns = [
    path('str',StoreHome.as_view(),name='storeh'),
    path('add',AddProduct.as_view(),name='addprod'),
    path("vpro",Productview.as_view(),name="vpro"),
    path('ed/<int:pk>',Edit.as_view(),name='editp'),
    path('del/<int:pk>',Deletep.as_view(),name='delp'),
    path("mypro",MyProductView.as_view(),name="myp"),
    path("cpass",CPassView.as_view(),name="cpass")
]
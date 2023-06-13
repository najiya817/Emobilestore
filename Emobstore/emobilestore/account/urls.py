from django.urls import path
from .views import RegView,LogOutView


urlpatterns = [
    path('reg/',RegView.as_view(),name='reg'),
    path('lout/',LogOutView.as_view(),name="lgout")
]
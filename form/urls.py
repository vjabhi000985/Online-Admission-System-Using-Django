from django.urls import path
from . import views

urlpatterns =[
path("appform1",views.appform1, name="appform1"),
path("payment",views.payment, name="payment"),
path("logout",views.logout, name="logout")
]
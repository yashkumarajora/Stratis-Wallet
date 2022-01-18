from django.contrib import admin
from django.urls import path
from wallet import views

urlpatterns = [
    path("",views.index, name='wallet'),
    path("index/",views.index, name='wallet'),
    path("login/",views.login,name='login'),
    path("main/",views.main,name='main'),
    path("newTxn/",views.newTxn,name='newTxn'),
    path("oldTxns/",views.oldTxn,name='oldTxns'),
    path("profile/",views.profile,name='profile'),
    path("signup/",views.signup,name='signup'),
    path("wallet/",views.wallet,name='wallet'),
    path("logout/",views.logoutpage,name='logout'),
]
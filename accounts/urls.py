from . import views
from django.urls import path


urlpatterns=[
            path('signup',views.signup,name='signup'),
            path('login',views.login,name='login'),
            path('mlogin',views.mlogin,name='mlogin'),
            path('msignup',views.msignup,name='msignup'),

            path('logout',views.logout,name='logout'),


]
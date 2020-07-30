from . import views
from django.urls import path


urlpatterns=[
            path('signup',views.signup,name='signup'),
            path('login',views.login,name='login'),
            path('mlogin',views.mlogin,name='mlogin'),

            path('logout',views.logout,name='logout'),
]
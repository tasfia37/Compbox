from . import views
from django.urls import path


urlpatterns=[
            path('create',views.create,name='create'),
            path('<int:complain_id>', views.detail, name='detail'),
            path('<int:complain_id>/deletecomplain', views.deletecomplain, name='deletecomplain'),
            path('m<int:complain_id>', views.mdetail, name='mdetail'),
            path('m<int:complain_id>/approvecomplain', views.approvecomplain, name='approvecomplain'),
            path('clist', views.clist, name='clist'),
            path('approvedlist', views.approvedlist, name='approvedlist'),
            # path('mclist', views.mclist, name='mclist'),
            path('mhome', views.mhome, name='mhome'),

]
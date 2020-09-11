from . import views
from django.urls import path



urlpatterns=[
            path('create',views.create,name='create'),
            path('<int:complain_id>', views.detail, name='detail'),
            path('m<int:complain_id>', views.mdetail, name='mdetail'),
            path('clist', views.clist, name='clist'),
            path('lastweek', views.lastweek, name='lastweek'),
            path('last15days', views.lastweek, name='last15days'),
            path('lastmonth', views.lastweek, name='lastmonth'),
            path('mhome', views.mhome, name='mhome'),
            path('ministrypage', views.getmins2, name='ministrypage'),
           # path('create', views.getmins, name='create'),

            path('<int:complain_id>/deletecomplain', views.deletecomplain, name='deletecomplain'),
            # path('mclist', views.mclist, name='mclist'),
            # path('mhome', views.getadd, name='add'),

            #tasfiar last add
            path('approvedlist', views.approvedlist, name='approvedlist'),
            path('m<int:complain_id>/approvecomplain', views.approvecomplain, name='approvecomplain'),
]
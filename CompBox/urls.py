from django.contrib import admin
from django.urls import path,include
#from . import views
from django.conf.urls.static import static
from django.conf import settings
from complain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('ministrypage/',views.ministrypage,name='ministrypage'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('accounts/',include('accounts.urls')),
   path('complain/',include('complain.urls'))


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

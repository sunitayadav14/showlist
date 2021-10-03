
from django.contrib import admin
from django.urls import path,include
from account.views import home 

from django.conf import settings
from django.conf.urls import url
from django.views.static import serve






urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('acc-',include(('account.urls','account'),namespace='account')),
    path('inc-',include(('todoapp.urls','todoapp'),namespace='todoapp')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

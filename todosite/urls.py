
from django.contrib import admin
from django.urls import path,include
from account.views import home 

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('acc-',include(('account.urls','account'),namespace='account')),
    path('inc-',include(('todoapp.urls','todoapp'),namespace='todoapp')),
]

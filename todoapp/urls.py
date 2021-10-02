
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('todoapp', v.add_list,name="addlist"),
    path('show', v.todo_show,name="showlist"),
    path('delete/<int:id>', v.delete_list,name="delist"),
]

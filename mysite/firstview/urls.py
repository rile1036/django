#from django.contrib import admin
from django.urls import path
from . import views #. 은 현재폴더

urlpatterns = [
    path('', views.index, name= 'index'),
    #path('admin/', admin.site.urls),
]


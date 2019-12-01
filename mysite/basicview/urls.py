#from django.contrib import admin
from django.urls import path
from . import views #. 은 현재폴더
import basic.views

urlpatterns = [
    path('login/', basicview.views.login, name= 'login'),
	path('basicview/signup/', basicview.views.signup, name= 'signup'),

    #path('admin/', admin.site.urls),
]


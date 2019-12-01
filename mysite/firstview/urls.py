#from django.contrib import admin
from django.urls import path
from . import views #. 은 현재폴더
import basicview.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name= 'index'),
	path('', basicview.views.login, name='login'),
	path('signup', basicview.views.signup, name='signup')
	#path('admin/', admin.site.urls),
]


#from django.contrib import admin
from django.urls import path
from . import views #. 은 현재폴더
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name= 'index'),
	path('', views.login, name='login'),
	path('signup', views.signup, name='signup'),
	path('logout', views.logout, name='logout'),
	path('new', views.new, name='new'),
	path('create', views.create, name='create'),
	path('detail/<int:people_id>', views.detail, name='detail'),
	path('detail/<int:people_id>/delete', views.delete, name='delete'),
	path('detail/<int:people_id>/edit', views.modify, name='modify')
	#path('basicview/admin/', basicview.views.admin)
]


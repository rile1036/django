from django.shortcuts import render
from django.http import HttpResponse

from .models import People

# Create your views here.
def index(request):
	peoples = People.objects.all()
	context = {'peoples':peoples}	

	return render(request, 'firstview/index.html', context)

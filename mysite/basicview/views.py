from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
#from .models import User
# Create your views here.
def login(request):
    return render(request, 'login.html')

def signup(request):
	if request.method == "POST":
		if request.POST["userPassword"] == request.POST["userPasswordConfirm"]:
			user = User.objects.create_user(
				userID=request.POST("userID"), userPassword=request.POST["userPassword"])
		#	auth.login(request, user)
			return redirect('index')
		return render(request, 'signup.html')
	return render(request, 'signup.html')

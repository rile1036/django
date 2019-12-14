from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
#from .models import User
#from django.contrib import auth
from .models import People
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def modify(request, people_id):
	people = People.objects.get(id = people_id)
	

def delete(request, people_id):
	people = People.objects.get(id = people_id)
	people.delete()
	return redirect('index')

def detail(request, people_id):
	people_detail = get_object_or_404(People, pk=people_id)
	return render(request, 'firstview/detail.html', {'people':people_detail})

def create(request):
	board = People()
	#board.number = timezone.datetime.now()
	board.name = request.GET['title']
	board.intro = request.GET['content']
	board.save()
	return redirect('index')
	#return render(request, 'firstview/index.html')

def new(request):
	return render(request, 'firstview/new.html')

def index(request):
	user = {'username': request.user, 'is_authenticated': request.user.is_authenticated}
	context2 = {'user':user}
	peoples = People.objects.all()
	context = {'peoples':peoples}	
	return render(request, 'firstview/index.html', context, context2)

def login(request):
	if request.method == "POST":
		ID = request.POST["userID"]
		Password = request.POST["userPassword"]
		usercheck = auth.authenticate(request, username=ID, password=Password)
		if usercheck is not None:
			auth.login(request, usercheck)
			return redirect('index')
		else:
			return render(request, 'login.html', {'error': 'incorrect'})
	return render(request, 'firstview/login.html')

def signup(request):
	if request.method == "POST":
		if request.POST["userPassword"] == request.POST["userPasswordConfirm"]:
			user = User.objects.create_user(
				username=request.POST["userID"], password=request.POST["userPassword"])
			#ID = request.POST["userID"]
			#Password = request.POST["userPassword"]
			#new_user = User(userID = ID, userPassword = Password)
			#new_user.save()
			auth.login(request, user)
			return render(request, 'login.html')
		return render(request, 'signup.html')
		#else:
		#	HttpResponse('비밀번호가 맞지 않습니다')
		#	return render(request, 'signup.html')
	return render(request, 'firstview/signup.html')

def logout(request):
	auth.logout(request)
	return redirect('login')

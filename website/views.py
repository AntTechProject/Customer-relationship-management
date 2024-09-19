from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        passowrd = request.POST['password']
        user = authenticate(request, username=username, password=passowrd)
        
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging In - Please Try Again'))
            return render(request, 'home.html', {})

    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout

# Create your views here.

def loginView(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('')
        else:
          
            return render(request, '')
    
    return render(request,'')


def logoutView(request):
    logout(request)
    return render(request,'')
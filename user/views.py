from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    
    return render(request,"user/login.html")
    

def login_view(request):
 
  if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          request.session['username'] = username
          request.session['logged_in'] = True
          return HttpResponseRedirect(reverse("index"))
         
      
     
      else:
          return render(request, "user/login.html",{
              "message": "Invalid credentials."
          })

  return HttpResponseRedirect(reverse("indexlogin"))
      

def logout_view(request):
    logout(request)
    request.session['logged_in'] = False
    return HttpResponseRedirect(reverse("index"))


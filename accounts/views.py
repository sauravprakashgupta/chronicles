from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        formObj=UserCreationForm(request.POST)
        if formObj.is_valid():
            user = formObj.save()
            #log the user in
            login(request,login)
            return redirect('articles:index')
    else:
        formObj = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':formObj})

def login_view(request):
    if request.method == "POST":
        formObj = AuthenticationForm(data=request.POST)
        if formObj.is_valid():
            user = formObj.get_user()
            login(request,user)
            # login is defined function in django
            return redirect('articles:index')
    else:
        formObj = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':formObj})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'accounts/login.html')

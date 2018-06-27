from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        formObj=UserCreationForm(request.POST)
        if formObj.is_valid():
            formObj.save()
            #log the user in
            return redirect('articles:index')
    else:
        formObj = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':formObj})

def login_view(request):
    if request.method == "POST":
        formObj = AuthenticationForm(data=request.POST)
        if formObj.is_valid():
            return redirect('articles:index')
    else:
        formObj = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':formObj})

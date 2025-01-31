from django.shortcuts import render, redirect
from django.contribution.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password']) #hash password
            user.save()
            login(request,user) #login the new user
            return redirect('home') #Redirect to home page
        else:
            form = RegisterForm()
        return render(request,'register.html',{'form':form})
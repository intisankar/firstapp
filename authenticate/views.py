from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm  ,PasswordChangeForm
from django.contrib import messages
from .forms import signup_form, EditProfileForm, RegisterForm

# Create your views here.
def index(request):
    return render(request,'authenticate/index.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You have been login!...'))
        # Redirect to a success page.
            return redirect('index')
        else:
            messages.success(request,('You are not registered..! '))
        # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request,'authenticate/login.html',{})    

def logout_user(request):
    logout(request)
    messages.success(request,('You are logout.!'))
    return redirect('login')

def register_user(request):
    if request.method =='POST':
        form = signup_form(request.POST)
        form1 = RegisterForm(request.POST)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            # for automatically login
            login(request,user)            
            messages.success(request,('You have been successfully registered'))
            return redirect('index')
    else:
        form = signup_form()
        form1 = RegisterForm()
    context = {'form': form,'form1':form1}
    return render(request,'authenticate/register.html',context=context)

def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You have been edited successfully!...'))
            return redirect('index')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request,'authenticate/edit_profile.html',context=context)

def  change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You have been edited password successfully!...'))
            return redirect('index')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request,'authenticate/change_password.html',context=context)

from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Post
from .forms import UserForm,UserUpdateForm,UpdateProfileForm
# Create your views here.
def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    form = UserForm()
    if request.method == 'POST':
        name = request.POST.get('username')
        code = request.POST.get('password')
        user = authenticate(request, username=name, password=code)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'User does not exist.')
    context = {'form':form,'page':page}
    return render(request,'blog/login_register.html',context)
def registerUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('home')
    else:
        form = UserForm()
    context = {'form':form}
    return render(request,'blog/register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')
def profile(request,pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=user)
        p_form = UpdateProfileForm(request.POST,request.FILES,instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account updated successfully')
            return redirect('profile',pk=user.id)
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = UpdateProfileForm(instance=user.profile)
    user = User.objects.get(id=pk)
    posts = user.post_set.all()
    context = {'user':user,'posts':posts,'u_form':u_form,'p_form':p_form}
    return render(request,'blog/profile.html',context)
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'blog/index.html',context)
def about(request):
    context = {}
    return render(request,'blog/about.html')
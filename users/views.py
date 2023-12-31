from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created.')
            return redirect('users:login-user')
        else:
            return render(request, 'users/register.html', {'form':form})
    else:
        form = RegisterUserForm()
        return render(request, 'users/register.html', {'form':form})
    
@login_required
def user_profile(request):
    return render(request, 'users/profile.html')
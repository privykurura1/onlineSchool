from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import login
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.refresh_from_db()
            new_user.username = form.cleaned_data.get('username')
            new_user.raw_password = form.cleaned_data.get('password1')
            new_user.is_mentor = form.cleaned_data.get('is_mentor')
            new_user.level = form.cleaned_data.get('level')
            new_user.save()
            user = authenticate(username=new_user.username, password=new_user.raw_password)
            login(request, new_user)
            return redirect('myblogs:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect("myblogs:index")





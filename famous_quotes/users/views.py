from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm

# Create your views here.

def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotesapp:index')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'signup.html', context={'form': form})
    return render(request, 'signup.html', context={'form': RegisterForm()})

def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotesapp:index')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')
        
        login(request, user)
        return redirect(to='quotesapp:index')
    return render(request, 'login.html', context={'form': LoginForm()})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotesapp:index')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    html_email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'password_reset_subject.txt'

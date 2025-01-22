from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . models import *
from . forms import *
from django.conf import settings
from django.core.mail import send_mail
import json
from django.http import JsonResponse
# Create your views here.

def userCreation(request):
    user = None
    error_message = None
    if request.POST:
        form = UserRegistrationForm(request.POST,request.FILES)
        username = request.POST['username']
        if form.is_valid():
            form.save()
            user = UserProfile.objects.get(username = username)
            if user:
                login(request,user)
                logged_user = UserProfile.objects.get(username = user)
                recipient_email = [logged_user.email]
                content = "You are successfully loggend in"
                subject = "Login"
                from_email = settings.EMAIL_HOST_USER
                try:    
                    send_mail(subject, content, from_email, recipient_email)
                except Exception as e:
                    print(e)
                    error_message = str(e)
                return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_security/registration.html', { 'form' : form, 'errors' : error_message })    


def userLogin(request):
    error_message = None
    user = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message = 'invalid credentials'
            return render(request, 'user_security/login.html',{'message':error_message})
    else:
        return render(request, 'user_security/login.html')
    
    
def userLogout(request):
    logout(request)
    return redirect('sign-in')

def forgotPasswordFunction(request):
    form = UserRegistrationForm()
    error_message = None
    if request.method == 'POST':
        print(request.content_type)
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            username = data['username']
            response_data = {
                'user' : username
            }
            request.session['username'] = username
            print('session value is set')
            return JsonResponse(response_data)
        else:
            username = request.session.get('username')
            user = UserProfile.objects.get(username = username)
            if(user):
                print(user)
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                if password1 == password2:
                    user.set_password(password1)
                    user.save()
                    return redirect('sign-in')
                else:
                    error_message = 'password mismatch'
                    print(form.errors)
            else:
                error_message = "invalid username"
    return render(request, 'user_security/forgot_password.html', { 'form' : form, 'error_message' : error_message })    
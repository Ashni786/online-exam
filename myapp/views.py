from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage, send_mail
from django.contrib.sessions.models import Session
# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.base import View

from myapp.models import UserProfile
from myapp.tokens import account_activation_token
from question.form import UserUpdate, ProfileUpdate



def hello(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')



def Login(request):
    if request.method == 'POST':
        un = request.POST['uname']
        pass1 = request.POST['pass2']
        user = auth.authenticate(username=un, password=pass1)
        if user is not None:
            auth.login(request, user)

            return render(request,'dashboard.html',)
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/login')
    else:
            return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/index')

def reg(request):
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        un = request.POST['uname']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']

        if pass1 == pass2:

            if User.objects.filter(username=un).exists():
                messages.info(request, 'Username already Taken')
                # print("Username Taken")
                return redirect('/register')
            elif User.objects.filter(email=em).exists():
                messages.info(request, "Email is Already Register")
                # print("Username Taken")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=un, email=em, password=pass1, first_name=fn, last_name=ln)
                user.is_active = False
                user.save()
                UserProfile.objects.create(user=user)
                # print('user created !')
                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                #user.email_user(subject, message)
                # send_mail(
                #     "Hello User",
                #     "Welcome to Email Confirmation",
                #     "corejavabtes@gmail.com",
                #     [em],
                #     fail_silently=False,
                # )
                send_mail(
                        subject,
                        message,
                        'btesinstitute74@gmail.com',
                        [em],
                        fail_silently=False,
                    )

                messages.success(request, ('Please Confirm your email to complete registration.'))
                return redirect('/login')

                # return render(request,'index.html')
                messages.info(request, 'You are Registered successfully !')
                return redirect('/login')

                # return render(request,'index.html')

        else:
            print('password not matched !')
            messages.info(request, 'register')

        return redirect('/register')

    else:

        return render(request, "register.html")

class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
            try:
                # uid = force_text(urlsafe_base64_decode(uidb64))
                uid = urlsafe_base64_decode(uidb64).decode()
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.profile.email_confirmed = True
                user.save()
                login(request, user)
                messages.success(request, ('Your account have been confirmed.'))
                print("confirmed", user.is_active)
                return render(request, 'index.html', {"data": user.first_name, "Flag": True})
            else:
                messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
                return redirect('/index')





#test
#from django.shortcuts import render

import urllib.request, json
def test(request):
    context = {}
    with urllib.request.urlopen(
            "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple") as url:
        data = json.loads(url.read().decode())
    document = data['results']
    context['document'] = document
    return render(request, 'test.html', context)




def exampattern(request):
    return render(request, 'exampattern.html')


@login_required(login_url='login')
def editprofile(request):
    if request.method=='POST':
        u_form = UserUpdate(request.POST,instance=request.user)
        p_form =  ProfileUpdate(request.POST,request.FILES,instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdate(instance=request.user)
        p_form =  ProfileUpdate(instance=request.user.userprofile)
    return render(request,'editprofile.html',{'u_form':u_form,'p_form':p_form})
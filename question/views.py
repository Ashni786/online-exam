from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash

from question.models import Questions, Feedback


@login_required(login_url='login')
def dash(request):

    return render(request, 'dashboard.html')

@login_required(login_url='login')
def categary(request):
    choices = Questions.CAT_CHOICES
    return render(request,'categary.html',{'choices': choices})

def questions(request , choice):
    if request.method == 'get':
        score = request.Get.get['score']
        print(score)
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    print(ques)
    return render(request,'questions.html',{'ques':ques})


@login_required(login_url='login')
def changepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            v = form.save()
            update_session_auth_hash(request, v)
            return HttpResponse("Password Change!")
    else:
        form =PasswordChangeForm(request.user)
    params= {
        'form':form,
    }
    return render(request,'changepass.html',params)

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='login')
def contact(request):
    return render(request,'contact-us.html')

@login_required(login_url='login')
def feedback(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        content=request.POST['content']
        feedback=Feedback(name=name, email=email, content=content)
        feedback.save()
        messages.success(request,'Thank you for  your feedback')
    return render(request,'feedback.html')


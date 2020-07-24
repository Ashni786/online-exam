from django.shortcuts import render
from quiz.models import Questions
def quiz(request):
    choices = Questions.CAT_CHOICES
    print(choices)
    return render(request,'quiz/home.html',{'choices':choices})
def quizquestions(request , choice):
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    return render(request,'quiz/questions.html',{'ques':ques})
def result(request):
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score  += 1
            #print(qid)
            #print(qans)
            #print(ans)
        print(score)

    return render(request, 'quiz/result.html',{'score':score, 'total':total})
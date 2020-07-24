from django.conf.urls import url,include
from django.contrib import admin
from quiz import views
app_name = "quiz"
urlpatterns = [
    url(r'^$', views.quiz, name = 'quiz'),
    url(r'^result', views.result, name = 'result'),
    url(r'^(?P<choice>[\w]+)', views.quizquestions, name = 'quizquestions'),
]

from django.conf.urls import url

from question import views

app_name = 'question'

urlpatterns = [
    url('dashboard/', views.dash, name="dashboard"),
    url('categary', views.categary,name="categary"),
    url('contact',views.contact, name="contact"),
    url('profile',views.profile,name="profile"),
    url('changepass',views.changepass,name="changepass"),
    url('feedback',views.feedback,name="feedback"),
    url(r'^(?P<choice>[\w]+)', views.questions, name='questions')



]
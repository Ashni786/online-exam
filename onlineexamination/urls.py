"""onlineexamination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from myapp.views import ActivateAccount
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.hello),
    path('index/', views.hello, name="index"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.Login, name="login"),
    path('about-us/', views.about, name="about"),
    path('register/', views.reg, name="reg"),
    path('editprofile/', views.editprofile),
    path('exampattern', views.exampattern, name="exampattern"),
    path('login/test/', views.test, name="test"),
    path('admin/', admin.site.urls),
    path('questions/', include('question.urls')),
    path('editprofile',views.editprofile,name="updateprofile"),

    # Password Reset

    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'),
         name='password_reset_complete'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'),
         name='password_reset_done'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)



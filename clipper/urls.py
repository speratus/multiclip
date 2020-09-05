from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import PasswordChangeForm
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('clipboard/', views.main, name='main'),
    path('logout/', views.signout, name='logout'),
    path('', TemplateView.as_view(template_name='clipper/index.html'), name='index'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='clipper/password_change.html',
        success_url='/clipboard/',
        form_class=PasswordChangeForm
    )),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view()),
    
]
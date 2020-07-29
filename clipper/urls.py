from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('clipboard/', views.main, name='main'),
    path('logout/', views.signout, name='logout'),
    path('', TemplateView.as_view(template_name='clipper/index.html'), name='index')
]
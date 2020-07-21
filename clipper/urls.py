from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('clipboard/', views.main, name='main'),
    path('logout', views.signout, name='logout')
]
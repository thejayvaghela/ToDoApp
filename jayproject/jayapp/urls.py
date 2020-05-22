from django.urls import path
from django.conf.urls import url
from jayapp.views import addTodoItem, completedTodoItem, deleteTodoItem, invalidlogin, todo, login, logout, my_auth, signup, signup_auth
from django.contrib.auth import views as auth_views
from django.contrib.admin import views

urlpatterns=[
    #path('', views.index),
    #url(r'^HomePageView/', views.HomePageView.as_view()),
    #path('Home/',views.home),
    url('Signup/$', signup),
    url('login/$', login),
    #url('auth/$', auth_view),
    url('myauth/$', my_auth),
    url('signup_auth/$', signup_auth),
    url('logout/$', logout),
    url('todo/$', todo),
    url('invalidlogin/$', invalidlogin),
    url('addTodoItem/$', addTodoItem),
    path('deleteTodoItem/<int:i>/', deleteTodoItem),
    path('completedTodoItem/<int:i>/', completedTodoItem),
]
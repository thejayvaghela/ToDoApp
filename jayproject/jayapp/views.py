from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect, request
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

from jayapp.models import User, TodoListItem

def signup(request):
    return render(request, 'signup.html')

def signup_auth(request):
    if request.method == "POST":
        fname=request.POST.get("first-name")
        lname=request.POST.get("last-name")
        email=request.POST["your-email"]
        password=request.POST["password"]
        cpassword=request.POST["confirm-password"]
        u=User(first_name=fname, last_name=lname, user_email=email, password=password)
        try:
            u_email=User.objects.get(user_email=email)
            return render(request, 'alreadyexists.html')
        except:
            u.save()
            request.session['email']=u.user_email                                  #   <----Session----
            request.session['first_name']=u.first_name
            context={
                'first_name':request.session['first_name']
            }
            return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def my_auth(request):
    email=request.POST.get("your-email")
    password=request.POST.get("password")
    try:
        u=User.objects.get(user_email=email)
        if email == u.user_email and password == u.password:
            request.session['email']=u.user_email                                  #   <----Session----
            request.session['first_name']=u.first_name
            return HttpResponseRedirect('/todo/')
        else:
            return render(request, 'invalidlogin.html')
    except:
        return render(request, 'invalidlogin.html')

def todo(request):
    u=User.objects.get(user_email=request.session['email'])
    all_todo_items = TodoListItem.objects.filter(user_email=u, status=False)
    completed_todo_items = TodoListItem.objects.filter(user_email=u, status=True)
    context={
         'first_name':request.session['first_name'] ,
         'all_items':all_todo_items,
         'completed_items':completed_todo_items,
    }
    return render(request,'home.html',context)

def addTodoItem(request):
    x=request.POST.get("content")
    y=request.session['email']
    new_item=TodoListItem(content=x,user_email=User.objects.get(user_email=y))
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodoItem(request, i):
    z=TodoListItem.objects.get(id=i)
    z.delete()
    return HttpResponseRedirect('/todo/')

def completedTodoItem(request, i):
    w=TodoListItem.objects.get(id=i, status=False)
    w.status = True
    w.date_completed=datetime.now()
    w.save()
    return HttpResponseRedirect('/todo/')

def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    #auth.logout(request)
    request.session['email']=None
    request.session['first_name']=None
    return render(request,'logout.html')
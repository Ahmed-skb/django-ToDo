from django.shortcuts import render, redirect
from .models import List

from .forms import ListForm
from django.contrib import messages, auth

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_item = List.objects.all()

            context = {
                'allItems': all_item
            }
            messages.success(request, ('Item Has Been Added To List!!'))
            return redirect("home")

    else:

        all_item = List.objects.all()

        context= {
            'allItems': all_item
        }
        return render(request, 'home.html', context)


def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!!'))
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    if item.completed == False:
        item.completed = True
    else:
        item.completed = False
    item.save()
    return redirect('home')

@login_required(login_url='login')
def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!!'))
            return redirect("home")
    else:
        item = List.objects.get(pk= list_id)

        context = {
            'item': item
        }
        return render(request, 'edit.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credential')
            return redirect('login')
    else:
        context={}
        return render(request, 'login.html', context)


def signup(request):
    if request.method == 'POST':
        #get all data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #password check
        if password == password2:
            #username is_exist check
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username has been taken!!')
                return redirect('signup')
            else:
                #email check
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email has being used!!')
                    return redirect('signup')
                else:
                    #create user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name = first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You Are now a register user.Login HERE!')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not matched!!')
            return redirect('signup')
    else:
        context = {}
        return render(request, 'signup.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out')
        return redirect('login')


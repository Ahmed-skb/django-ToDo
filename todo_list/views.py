from django.shortcuts import render, redirect
from .models import List

from .forms import ListForm
from django.contrib import messages

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


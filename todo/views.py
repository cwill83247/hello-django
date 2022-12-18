from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):  # take a http request from user
    items = Item.objects.all()
    context = {
        'items':  items
    }
    return render(request, 'todo/todo_list.html',context )  # returns the todolist page


def add_item(request):  # take a http request from user  
    if request.method == 'POST':
        form =ItemForm(request.POST)        #django form option
        if form.is_valid():                 #django form option
             form.save()                    #django form option
             return redirect('get_todo_list')             # redirect to the function 
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)     # if its a get reqeust jsut returns add_item page

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form =ItemForm(request.POST, instance=item)        #django form option
        if form.is_valid():                 #django form option
             form.save()                    #django form option
             return redirect('get_todo_list')             # redirect to the function 

    form = ItemForm(instance=item)                      # without instance=item form isn't prefilled with the data 
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)

def toggle_item(request,item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done 
    item.save()
    return redirect('get_todo_list')

def delete_item(request,item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')


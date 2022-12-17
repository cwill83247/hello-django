from django.shortcuts import render, HttpResponse, redirect
from .models import Item

# Create your views here.


def get_todo_list(request):  # take a http request from user
    items = Item.objects.all()
    context = {
        'items':  items
    }
    return render(request, 'todo/todo_list.html',context )  # returns the todolist page


def add_item(request):  # take a http request from user  
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST                # this is different because is a checkbox value we are checking
        Item.objects.create(name=name, done=done)      # in out Items Table > create > use variables above and apply to table values 

        return redirect('get_todo_list')             # redirect to the function 

    return render(request, 'todo/add_item.html')     ##if its a get reqeust jsut returns add_item page







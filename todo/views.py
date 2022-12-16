from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.


def get_todo_list(request):  # take a http request from user
    items = Item.objects.all()
    context = {
        'items':  items
    }
    return render(request, 'todo/todo_list.html',context )  # returns the todolist page





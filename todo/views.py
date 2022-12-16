from django.shortcuts import render, HttpResponse

# Create your views here.
def get_todo_list(request):  # take a http request from user
    return render(request, 'todo/todo_list.html')  # returns the todolist page




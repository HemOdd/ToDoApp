from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoTask

# Create your views here.
def todoView(request):
    items = todoTask.objects.all()
    return render(request,'todoList.html',{'allItems': items})

def addTask(request):
     newContent = request.POST['content']
     newTask = todoTask(content = newContent)
     newTask.save()
     return HttpResponseRedirect('/home/')

def removeTask(request,item_id):
    delItem = todoTask.objects.get(id = item_id)
    delItem.delete()
    return HttpResponseRedirect('/home/')
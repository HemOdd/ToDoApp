from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import todoTask


class ToDoView(View):
     
     def get(self,request):
          items = todoTask.objects.all()
          return render(request,'todoList.html',{'allItems': items})

class SubmitTask(View):

     def post(self,request):
          newContent = request.POST['content']
          newTask = todoTask(content = newContent)
          newTask.save()
          return HttpResponseRedirect('/home/')

class RemoveTask(View):

     def post(self,request, item_id):
          delItem = todoTask.objects.get(id = item_id)
          delItem.delete()
          return HttpResponseRedirect('/home/')    
  




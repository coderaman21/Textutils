from django.shortcuts import render
from .models import Task
# Create your views here.
def index(request):
    success = False
    if request.method == 'POST':
        title = request.POST['title'].lower()
        desc = request.POST['desc']
        task = Task(taskTitle = title , taskdesc = desc)
        task.save()
        success = True
    return render(request,'index.html' , {"success":success})

def search(request):
    if request.method == 'GET':
        success = True
        query = request.GET.get('search').lower()

        task = Task.objects.filter(taskTitle = query)
        if task:
            tasks_list =[]
            for i in task:
                tasks_list.append(i)
            return render(request,'search.html',{'query':query,'success':success,'tasks':tasks_list})
        
        else:
            success = False
            return render(request,'search.html',{'query':query,'success':success})
        

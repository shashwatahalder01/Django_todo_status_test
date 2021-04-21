from django.shortcuts import render, HttpResponse
from django import forms
from .forms import todoform
from .models import todo
# Create your views here.


def todotest(requests):

    form = todoform(requests.POST or None)
    if requests.method == 'POST':
        if form.is_valid():
            taskname = form.cleaned_data.get("taskname").lower()
            status = form.cleaned_data.get("status").lower()


            # todo.objects.all().delete()

            dbdata = todo(taskname=taskname,taskstatus=status)
            dbdata.save()


            a= todo.objects.filter(taskname=taskname)

            for item in a:
                t=item.taskname
                status=item.taskstatus

            t = taskname
            if status=='inprogress':
                progress=t+" is in progress"
                done=""
                complete=""
            elif status =='done':
                progress=''
                done = t+" is Done"
                complete=""
            elif status=='complete':
                progress=''
                done=""
                complete = t+" is completed"
            
            html = {'title': 'TODO', 'form':form,'isinprogress': progress,
                    'isdone': done, 'iscomplete': complete}
            link = 'todo/todo.html'
            return render(requests, link, html)

    else:
        html = {'title': 'TODO', 'form':form}
        link = 'todo/todo.html'
        return render(requests, link, html)

from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})


def edit(request, id):
    try:
        ts = Task.objects.get(id=id)
        if request.method == 'POST':
            ts.body = request.POST.get('body')
            ts.save()
            return redirect('/')
        else:
            return render(request, 'main/edit.html', {'ts': ts})
    except Task.DoesNotExist:
        return HttpResponseNotFound("Задача не найдена")


def delete(request, task_id):
    ts = Task.objects.get(id=task_id)
    ts.delete()
    return redirect('/')

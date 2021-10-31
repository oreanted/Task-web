from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Query
from .forms import TaskForm, QueryForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


@login_required()
def list(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.users = request.user
            instance.save()
        messages.success(request, ("New task added!"))
        return redirect('list')
    else:
        all_task = Task.objects.filter(users=request.user)
        paginator = Paginator(all_task, 8)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_task': all_task})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.users == request.user:
        task.delete()
    else:
        messages.error(request, ("Access Restricted! You Are Not Allowed!"))
    return redirect('list')


def edit_task(request, task_id):
    if request.method == "POST":
        task_obj = Task.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task Edited !"))
        return redirect('list')
    else:
        task_obj = Task.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})


def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.users == request.user:

        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Restricted! You Are Not Allowed!"))
    return redirect('list')


def pending_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('list')


@login_required()
def contact(request):

    if request.method == "POST":
        form = QueryForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('contact')
    else:
        query = Query.objects.all
        return render(request, 'contact.html', {'query': query})


def delete_query(request, query_id):
    query1 = Query.objects.get(pk=query_id)
    query1.delete()
    return redirect('contact')


def about(request):
    context = {}
    return render(request, 'about.html', context)

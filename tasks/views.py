from traceback import format_exc

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def home(request):




def create_task(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task_detail.html', {'task': task})


def detail_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'task Has Been Created Successfully')
            return redirect('home')

    return render(request, 'product_form.html', {'form': form})

def delete_task(request, id):
    product = get_object_or_404(Task, id=id)
    form = TaskForm(instance=Task)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=Task)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'task Has Been Updated Successfully')
            return redirect('home')
    return render(request, 'task_form.html', {'form': form})

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.add_message(request, messages.SUCCESS, 'Product Has Been Deleted Successfully')
    return redirect('home')







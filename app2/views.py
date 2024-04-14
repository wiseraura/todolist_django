from django.shortcuts import render, redirect
from .models import User, Task

# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def task_list(request):
    tasks = Task.objects.all()
    users = User.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks,'users': users})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

def create_task(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    due_date = request.POST.get('due_date')
    assigned_user_id = request.POST.get('assigned_user')

    new_task = Task(title=title, description=description, due_date=due_date)
    if assigned_user_id:
        try:
            assigned_user = User.objects.get(id=assigned_user_id)
            assigned_user.save()
            new_task.user = assigned_user
        except User.DoesNotExist:
            return render(request, 'task_form.html', {'error_message': 'Invalid user selected'})

    new_task.save()
    tasks = Task.objects.all()
    users = User.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks,'users': users})



from django.shortcuts import render, redirect, HttpResponse
from home.models import Task

def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        # Ensure both title and description are provided
        if title and desc:
            ins = Task(taskTitle=title, taskDesc=desc)
            ins.save()
            print("Task added successfully.")
            return HttpResponse("Form submitted successfully.")  # Return success message
        else:
            return HttpResponse("Please fill in all required fields.")  # Return error message if fields are missing

    return render(request, 'index.html')

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

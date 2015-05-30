from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template import RequestContext
from django.conf import settings
from lists.forms import TaskForm
from lists.models import Task
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

def home_page(request):
	return HttpResponse('Iam here')


def index_page(request):
	return render_to_response('index.html', context_instance = RequestContext(request))


def add_task(request):
	
	message = ""
	if request.method == "POST":
		form = TaskForm(request.POST)
		
		if form.is_valid():
			form.save()
			message = "Task added Successfully"

	else:
		form = TaskForm()

	return render_to_response('addtask.html', {'form': form, 'message':message}, context_instance=RequestContext(request))


def edit_task(request, task_id):
	
	message = ""
	task = get_object_or_404(Task, id = task_id)
	if request.method == "POST":
		
		form = TaskForm(request.POST, instance = task)
		
		if form.is_valid():
			form.save()
			message = "Task Edited Successfully"

	else:
		form = TaskForm(instance = task)

	return render_to_response('edittask.html', {'form': form, 'message': message, 'task': task}, context_instance=RequestContext(request))


def task_list(request):
	tasks = Task.objects.all()
	return render_to_response('tasklist.html', {'tasks': tasks}, context_instance=RequestContext(request))

def delete_task(request, task_id):
	task = get_object_or_404(Task, id = task_id)
	task.delete()
	return HttpResponseRedirect('/task-list/')
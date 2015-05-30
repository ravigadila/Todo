from django import forms
from lists.models import Task
from django.contrib.admin import widgets


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['Title','Description', 'due_time']

	def __init__(self, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['due_time'].widget = widgets.AdminSplitDateTime()
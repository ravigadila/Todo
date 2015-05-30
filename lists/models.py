from django.db import models

# Create your models here.

class Task(models.Model):

	Title = models.CharField(max_length = 55)
	Description = models.TextField()
	due_time = models.DateTimeField(auto_now = False, null = True, blank = True)

	def __unicode__(self):
		return self.Title

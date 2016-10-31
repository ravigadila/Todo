from django.db import models

# Create your models here.

class Task(models.Model):

	Title = models.CharField(max_length = 55, verbose_name='name')
	Description = models.TextField()
	due_time = models.DateTimeField(auto_now = False, null = True, blank = True)

	def __unicode__(self):
		return self.Title

	def get_readable_due_date(self):
		value = self.due_time
		return value.strftime("%B %d, %Y %H:%M:%S")


class Group_task(models.Model):

	group_name = models.CharField(max_length = 55)
	Description = models.TextField()

	def __unicode__(self):
		return self.group_name
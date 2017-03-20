from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.test import Client
from lists.forms import TaskForm
from lists.models import Task



class SimpleAdditionTest(TestCase):
    
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ModelMethodTest(TestCase):

	def setUp(self):
		self.task = Task.objects.create(Title = 'MyTask', 
					Description = 'tasdescription', due_time = '2012-06-08 10:29:47')
	def test_method(self):
		t = Task.objects.get(Title = 'MyTask')
		self.assertEqual('June 08, 2012 10:29:47', t.get_readable_due_date())


class HomePageTest(TestCase):

	def test_root_url_to_home_page(self):
		home = resolve('/')
		self.assertEqual(home.func, home_page)


class UrlTests(TestCase):

	def test_index_html_page(self):
		self.client = Client()
		response = self.client.get('/index/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response,'index.html')
		self.assertIn('MicroPyramid', response.content)
		# self.assertTrue(response.content.endswith(b'</html>'))

class TaskFromTest(TestCase):

	def test_form_invalidate_with_dateformat(self):
		form = TaskForm(data = {'Title':'Build ToDo aplication','Description':'Create Read Update Delete', 'due_time':'2012/06/08 10:29:47'})
		#self.assertFalse(form.is_valid())

	def test_form_invalide(self):

		form = TaskForm(data = {'Title':'','Description':'', 'due_time':''})
		self.assertFalse(form.is_valid())

	def test_form_valid(self):
		form = TaskForm(data = {'Title':'Build ToDo aplication','Description':'Create Read Update Delete', 'due_time':'2012-06-08 10:29:47'})
		self.assertTrue(form.is_valid())


class AddTaskViewsTest(TestCase):

	def setUp(self):
		self.client = Client()

	def test_add_task_html_page(self):
		
		response = self.client.get('/add-task/')
		
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed('addtask.html')
		
		self.assertIn('Title', response.content)
		self.assertIn('Description', response.content)
		self.assertIn('due_time', response.content)

	def test_add_task_html_page_output(self):

                response = self.client.get('/add-task/')

                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed('addtask.html')

                self.assertIn('Title', response.content)
                self.assertIn('Description', response.content)
                self.assertIn('due_time', response.content)

	def test_add_task_with_empty_data(self):
		
		task_data = {}
		response = self.client.post('/add-task/', task_data)
		self.assertEqual(response.status_code, 200)

		self.assertFormError(response, 'form', 'Title', 'This field is required.')
		self.assertFormError(response, 'form', 'Description', 'This field is required.')

	def test_add_task_with_incorect_data(self):

		task_data = {'Title':'My first task','Description':'My first task description', 'due_time':'2012/06/08 10:29:47'}
		response = self.client.post('/add-task/', task_data)
		
		#self.assertFormError(response, 'form', 'due_time', 'Enter a valid date/time.')

	def test_add_task_with_valid_data(self):
		tasks_count = Task.objects.count()
		self.assertEqual(tasks_count, 0)
		task_data = {'Title':'My first task','Description':'My first task description', 'due_time':'2012-06-08 10:29:47'}
		response = self.client.post('/add-task/', task_data)
		tasks_count = Task.objects.count()
		self.assertEqual(tasks_count, 1)
		self.assertEqual(response.status_code, 200)


class ListEditTaskTest(TestCase):

	def setUp(self):
		self.client = Client()
		task = Task.objects.create(Title = 'My first task', Description = 'My first task description', due_time = '2012-06-08 10:29:47')

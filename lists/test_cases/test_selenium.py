from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class BaseTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
        cls.driver.quit()

class AddTaskTestCase(BaseTestCase):


	def test_add_task(self):
		self.driver.get(self.live_server_url + '/add-task/')
		self.driver.find_element_by_id('id_Title').send_keys('NewTask')
		self.driver.find_element_by_id('id_Description').send_keys('NewTaskDiscription')
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		self.assertTrue(self.driver.find_element_by_id('result-message').text.startswith('Task added Successfully'))

from django.test import LiveServerTestCase
from pyvirtualdisplay import Display
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class BaseTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.display = Display(visible=0, size=(800, 600))
        cls.display.start()
        cls.driver = WebDriver()
        super(BaseTestCase, cls).setUpClass()
        

    @classmethod
    def tearDownClass(cls):
        super(BaseTestCase, cls).tearDownClass()
        cls.driver.quit()
        cls.display.stop()

class AddTaskTestCase(BaseTestCase):


	def test_add_task(self):
		self.driver.get(self.live_server_url + '/add-task/')
		self.driver.find_element_by_id('id_Title').send_keys('NewTask')
		self.driver.find_element_by_id('id_Description').send_keys('NewTaskDiscription')
		self.driver.find_element_by_css_selector("input[type=submit]").click()
		self.assertTrue(self.driver.find_element_by_id('result-message').text.startswith('Task added Successfully'))

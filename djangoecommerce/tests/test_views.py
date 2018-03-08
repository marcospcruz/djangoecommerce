from django.test import TestCase, Client

class IndexViewTestCase:
	def test_status_code(self):
		client=Client()
		response = client.get('/')
		
		
	def test_template_used(self):
		runTest('/cu')
		
	def runTest(url):
		self.assertEquals(response.status_code,200)
	
	def setup(self):
		self.client=Client()
		
	def tearDown(self):
		pass
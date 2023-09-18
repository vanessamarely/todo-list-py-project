from django.test import TestCase
from todoapp.models import Todo

class IntegrationTestCase(TestCase):
    def test_integration(self):
        # Create a test todo object
        todo = Todo.objects.create(title='Test Todo')

        # Simulate a POST request
        response = self.client.post('/', {'title': 'New Todo'})

        # Check if the response is a redirect
        self.assertRedirects(response, '/')

        # Check if the new todo was saved
        new_todo = Todo.objects.get(title='New Todo')
        self.assertEqual(new_todo.title, 'New Todo')

        # Check if the old todo still exists
        self.assertTrue(Todo.objects.filter(title='Test Todo').exists())

        # Check if the todos are passed to the template
        response = self.client.get('/')
        self.assertContains(response, 'New Todo')
        self.assertContains(response, 'Test Todo')
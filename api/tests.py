from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import User, Task


class TaskViewsTest(TestCase):
    def setUp(self):
        # Criar um usuário de teste
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Criar um token de autenticação
        self.token = Token.objects.create(user=self.user)
        # Criar uma task de teste associada ao usuário
        self.task = Task.objects.create(title='Test Task', description='Test Description', user=self.user, status='pendente')
        # Criar um cliente para fazer requisições
        self.client = APIClient()
       

    # Testa se a view retorna a task correta
    def test_get_task_by_id(self):
        # Define o cabeçalho de autorização com o token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('get_task_by_id', kwargs={'id': self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')
        self.assertEqual(response.data['description'], 'Test Description')

    # Testa se a view retorna 404 quando a task não é encontrada
    def test_get_task_by_id_not_found(self):
        url = reverse('get_task_by_id', kwargs={'id': 999})  # ID que não existe
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Create your tests here.

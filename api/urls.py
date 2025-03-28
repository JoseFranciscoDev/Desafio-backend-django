from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    #endpoints para pegar o token de autenticação
    path('token/', TokenObtainPairView.as_view(), name= 'token_autentication'), #token de autenticacao
    path('token/refresh/', TokenRefreshView.as_view()),
    
    #endpoints tasks
    path('tasks/', views.get_tasks, name='get_tasks',),  # Lista todas as tasks
    path('tasks/<int:id>/', views.get_task_by_id, name='get_task_by_id'),  # Busca uma task pelo id_user
    path('tasks/status/<str:status_task>/', views.get_tasks_by_status, name='get_tasks_by_status'), # Busca tasks pelo status
    path('tasks/create/', views.create_task, name='create_task'),  # Cria uma task
    path('tasks/update/<int:id>/', views.update_task, name='update_task'), # Atualizar task pelo ID
    path('tasks/delete/<int:id>/', views.delete_task, name='delete_task'), # deletar tarefa pelo ID
    
    #endpoints users
    path('users/', views.get_users, name='get_users'),  # Lista todos os usuários
    path('users/<int:id>/', views.get_user_by_id, name='get_user'),  # Busca um usuário pelo ID
    path('users/create/', views.create_user, name = 'create_user'),  # Cria um usuário
    path('users/delete/<int:id>/', views.delete_user, name='delete_user'), #deletar usuario pelo ID
    path('users/<int:user_id>/tasks/', views.get_tasks_by_user_id, name='get_tasks_by_user_id') #Busca todas as tasks do usuario pelo ID
]


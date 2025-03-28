from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from .models import User

#Views tasks:
# Listar todas as tasks do usuário autenticado:
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    # Obtém o usuário autenticado
    user = request.user
    # Filtra as tasks associadas ao usuário
    tasks = Task.objects.filter(user=user)
    # Configura a paginação das tasks
    paginator = PageNumberPagination()
    paginator.page_size = 10  # Define o número de tasks por página
    result_page = paginator.paginate_queryset(tasks, request)
    # Serializa os dados das tasks
    serializer = TaskSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)  # Retorna a resposta paginada

# Buscar uma task pelo ID:
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task_by_id(request, id):
    try:
        # Tenta obter a task pelo ID e verificar se pertence ao usuário autenticado
        task = get_object_or_404(Task, id=id, user=request.user)
    except:
        # Retorna erro 404 se a task não for encontrada
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Serializa os dados da task
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)  # Retorna a task encontrada

# Buscar todas as tasks do usuário filtradas por status:
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks_by_user_id(request, user_id):
    try:
        # Filtra as tasks pelo user_id e ordena pelo título
        tasks = Task.objects.filter(user_id=user_id).order_by('title')
    except:
        # Retorna erro 404 se as tasks não forem encontradas
        return Response(status=status.HTTP_404_NOT_FOUND)     
    # Serializa as tasks filtradas
    serializer = TaskSerializer(list(tasks), many=True) 
    return Response(serializer.data, status=status.HTTP_200_OK)

# Buscar tasks filtradas por status:
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks_by_status(request, status_task):
    try:
        # Obtém o usuário autenticado
        user = request.user
        # Filtra as tasks pelo status fornecido na URL
        tasks = Task.objects.filter(status=status_task, user=user).order_by('title')    
        # Serializa as tasks filtradas
        serializer = TaskSerializer(list(tasks), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
# Criar uma nova task:
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    # Obtém o usuário autenticado
    user = request.user  
    # Obtém os dados da nova task do corpo da requisição
    new_task_data = request.data 
    new_task_data['user'] = user.id  # Associa a task ao usuário autenticado
    # Serializa os dados da task
    serializer = TaskSerializer(data=new_task_data)
    if serializer.is_valid():
        # Salva a task associada ao usuário
        serializer.save(user=user)  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Retorna erro caso a serialização não seja válida
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Atualizar uma task existente:
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, id):
    try:
        # Tenta obter a task pelo ID e verificar se pertence ao usuário autenticado
        task = Task.objects.get(id=id, user = request.user)
    except: 
        # Retorna erro 404 caso a task não seja encontrada
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Serializa a task com os novos dados fornecidos
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        # Salva a task atualizada
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

# Deletar uma task:
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, id):
    try:
        # Tenta obter a task pelo ID e verificar se pertence ao usuário autenticado
        task = Task.objects.get(id=id, user=request.user)
    except Task.DoesNotExist:
        # Retorna erro 404 se a task não for encontrada ou não pertencer ao usuário
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Deleta a task
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Views para os usuários:

# Listar todos os usuários:
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    # Obtém todos os usuários do sistema
    users = User.objects.all()
    # Serializa os dados dos usuários
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Buscar usuário pelo ID:
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_by_id(request, id):
    try:     
        # Tenta obter o usuário pelo ID
        user = User.objects.get(id=id)
    except:
        # Retorna erro 404 caso o usuário não seja encontrado
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Serializa os dados do usuário
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Criar um novo usuário:
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    # Obtém os dados do novo usuário do corpo da requisição
    new_user = request.data
    password = new_user.get('password')  # Extrai a senha
    # Serializa os dados do novo usuário
    serializer = UserSerializer(data=new_user)     
    if serializer.is_valid():
        # Cria o usuário e configura a senha de forma segura
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # Retorna erro caso a serialização não seja válida
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deletar um usuário:
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, id):
    try:
        # Tenta obter o usuário pelo ID
        user = User.objects.get(id=id)
    except:
        # Retorna erro 404 caso o usuário não seja encontrado
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Serializa os dados do usuário a ser excluído
    serializer = UserSerializer(user)
    # Deleta o usuário
    user.delete()
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework.pagination import PageNumberPagination

from .models import Task
from .serializers import TaskSerializer, UserSerializer
from .models import User

#Views tasks:
#listar todas as tasks:
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    user = request.user
    tasks = Task.objects.filter(user = user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
#buscar uma task pelo ID:
@api_view(['GET'])
def get_task_by_id(request, id):
    try:
        task = Task.objects.get(id = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)
        
#busca todas as tasks do usuario pelo user_id        
@api_view(['GET'])
def get_tasks_by_user_id(request, user_id):
    status_task = request.GET['status']
    try:
        tasks = Task.objects.filter(user_id = user_id).order_by('title')
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)     
    serializer = TaskSerializer(list(tasks), many=True) 
    return Response(serializer.data, status=status.HTTP_200_OK)

#busca tasks por status
@api_view(['GET'])
def get_tasks_by_status(request, status_task):
    try:
        tasks = Task.objects.filter(status = status_task).order_by('title')
        serializer = TaskSerializer(list(tasks), many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

#criar uma task:    
@api_view(['POST'])
def create_task(request):
    user = request.user  
    new_task_data = request.data.copy() 
    new_task_data['user'] = user.id
    serializer = TaskSerializer(data=new_task_data)
    if serializer.is_valid():
        serializer.save(user=user)  # Salva a task associada ao usuário autenticado
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# atualizar uma task:
@api_view(['PUT'])
def update_task(request, id):
    try:
        task = Task.objects.get(id = id)
    except: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# deletar uma task:
@api_view(['DELETE'])
def delete_task(request, id):
    try:
        task = Task.objects.get(id = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(Task.objects.all())
    task.delete()
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


#Views users:
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
   
# buscar usuario pelo ID
@api_view(['GET'])
def get_user_by_id(request, id):
    try:     
        user = User.objects.get(id = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    print('view user/id')
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_user(request):
    new_user = request.data
    password = new_user.get('password')
    serializer = UserSerializer(data = new_user)     
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(id = id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    user.delete()
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

# Create your views here.

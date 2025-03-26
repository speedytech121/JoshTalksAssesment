from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, User
from .serializers import UserSerializer, TaskSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from django.db import transaction
# from django.contrib.auth.models import User


class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                name=serializer.validated_data['name'],
                email=serializer.validated_data.get('email', ''),
                mobile=str(serializer.validated_data.get('mobile', ''))
            )

            return Response({'message': 'User created successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# API to create a task
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# API to assign a task to users

class AssignTaskView(APIView):
    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            user_ids = request.data.get('user_ids', [])

            # Ensure user_ids is a list of integers
            if not isinstance(user_ids, list) or not all(isinstance(i, int) for i in user_ids):
                return Response({"error": "Invalid format. 'user_ids' must be a list of integers."}, status=status.HTTP_400_BAD_REQUEST)

            # Fetch valid user IDs from the database
            valid_users = User.objects.filter(id__in=user_ids)
            valid_user_ids = list(valid_users.values_list('id', flat=True))

            if not valid_user_ids:
                return Response({"error": "No valid user IDs found."}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():  # Ensure database integrity
                task.users.set(valid_user_ids)  # ✅ Assign only valid users

            return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
# API to get tasks assigned to a user
class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = int(self.kwargs['user_id'])
        return Task.objects.filter(users__id=user_id)

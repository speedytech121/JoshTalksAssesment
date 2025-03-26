from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source = 'id', read_only = True)
    class Meta:
        model = User
        fields = ['user_id','name','email','mobile']

class TaskSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(source='id', read_only = True)
    users_allocated = UserSerializer(source='users', many=True, read_only=True)  # Include user details in response
    user_ids = serializers.ListField(write_only=True, child=serializers.IntegerField(), required=False)

    class Meta:
        model = Task
        fields = ['task_id', 'name', 'description', 'created_at', 'completed_at', 'status', 'users_allocated', 'user_ids']

    def create(self, validated_data):
        user_ids = validated_data.pop('user_ids', []) # Includes an extra user_ids field to assign users when creating tasks.
        task = Task.objects.create(**validated_data)
        task.users.set(user_ids)  # Assign users to the task
        return task

from django.urls import path
from .views import TaskCreateView, AssignTaskView, UserTasksView, CreateUserView

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create-task'),
    path('<int:task_id>/assign/', AssignTaskView.as_view(), name='assign-task'),
    path('user/<int:user_id>/', UserTasksView.as_view(), name='user-tasks'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),  # ✅ New User Creation API
]

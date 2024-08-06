from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete
urlpatterns = [
     path('', TaskList.as_view(), name='task'),
    path('tasks-create/', TaskCreate.as_view(), name='tasks-create'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks-update/<int:pk>/', TaskUpdate.as_view(), name='tasks-update'),
    path('tasks-delete/<int:pk>/', TaskDelete.as_view(), name='tasks-delete'),


]
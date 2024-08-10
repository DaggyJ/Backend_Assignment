from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLonginView, RegisterPage, CustomLogoutView
#from django.contrib.auth.views import LogoutView


urlpatterns = [
     path('', TaskList.as_view(), name='task'),
    path('tasks-create/', TaskCreate.as_view(), name='tasks-create'),
    path('login/', CustomLonginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks-update/<int:pk>/', TaskUpdate.as_view(), name='tasks-update'),
    path('tasks-delete/<int:pk>/', TaskDelete.as_view(), name='tasks-delete'),

]
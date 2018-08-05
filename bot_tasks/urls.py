from django.urls import path
from bot_tasks import views

app_name = 'bot_tasks'

urlpatterns = [
    path('', views.PendingTasks.as_view(), name='pending-tasks'),
    # TODO -> Need to update this to each individual task..
    path('<slug:slug>/new_task/', views.TaskCreateView.as_view(), name='task-create')
]

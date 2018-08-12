from django.urls import path
from bot_tasks import views

app_name = 'bot_tasks'

urlpatterns = [
    path('', views.PendingTasks.as_view(), name='pending-tasks'),
    path('<slug:slug>/select_task/', views.TaskSelectView.as_view(), name='task-select'),
    # TODO -> Each of the individual tasks
    path('<slug:slug>/new_unfollow_non_followers_task/', views.CreateUnfollowNonFollowersTask.as_view(), name='create-unfollow-non-followers-task')
]

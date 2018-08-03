from django.urls import path
from bot_tasks import views

app_name = 'bot_tasks'

urlpatterns = [
    path('', views.PendingOperations.as_view(), name='pending-operations')
]

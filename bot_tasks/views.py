from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from bot_tasks.models import (
    BotTask,
    UnfollowNonFollowersTask
)

class PendingTasks(ListView):
    model = BotTask
    context_object_name = 'bot_task_list'
    template_name = 'bot_tasks/bot_tasks.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PendingOperations, self).get_context_data(**kwargs)
        title = 'Recent pending operations'
        return context

    def get_queryset(self, *args, **kwargs):
        # TODO -> Filter by the user
        queryset = BotTask.objects.all()
        return queryset


class TaskSelectView(TemplateView):
    """
    A template view that allows users to select which type of task
    they want to create.
    """
    template_name = 'bot_tasks/task_to_create.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TaskSelectView, self).get_context_data(*args, **kwargs)
        return context

class CreateUnfollowNonFollowersTask(FormView):
    pass

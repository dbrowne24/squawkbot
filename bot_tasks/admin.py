from django.contrib import admin
from bot_tasks.models import UnfollowNonFollowersTask

bot_tasks_models = [
    UnfollowNonFollowersTask
]

admin.site.register(bot_tasks_models)

from django.core.management.base import BaseCommand, CommandError
# TODO -> I'm not sure if I should be pulling in each individual model
from bot_tasks.models import BotTask

class Command(BaseCommand):
    help = 'Handles all of the bot tasks'

    def __init__(self, *args, **kwargs):
        self.task_list = BotTask.objects.filter(task_status=BotTask.PENDING)
        super(BaseCommand, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        print("[+] Processing a list of tasks")
        for task in self.task_list:
            try:
                print("[+] Running a task")
            except:
                print("[+] The task has failed")

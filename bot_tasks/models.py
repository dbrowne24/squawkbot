from django.db import models

from twitter_accounts.models import TwitterAccount


class BotTask(models.Model):
    """
    An abstract base class that we can extends for each type of bot operation
    that we want to create...
    """
    PENDING = 'PD'
    COMPLETE = 'CP'
    FAILED = 'FD'

    TASK_STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed'),
    )

    twitter_account = models.ForeignKey(TwitterAccount, on_delete=models.CASCADE)
    task_status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES)
    task_name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.task_name

    def __str__(self):
        return self.task_name


class UnfollowNonFollowersTask(BotTask):
    """
    Inherits from BotTask

    This bot task defines an operation that will unfollow any accounts
    that the twitter account is following, if they don't also follow the account
    """
    pass

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify


class TwitterAccount(models.Model):
    """
    Defines a twitter account
    """
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # TODO We are not currently creating a slug
    slug = models.SlugField(unique=True)
    consumer_key = models.CharField(max_length=300)
    consumer_secret = models.CharField(max_length=300)
    access_token = models.CharField(max_length=300)
    access_secret = models.CharField(max_length=300)
    twitter_handle = models.CharField(max_length=300)

    def __unicode__(self):
        return self.twitter_handle

    def __str__(self):
        return self.twitter_handle

    def get_delete_url(self):
        return reverse('twitter_accounts:twitter-account-delete', kwargs={'slug': self.slug })

    def get_create_task_url(self):
        return reverse('bot_tasks:task-select', kwargs={'slug': self.slug })


def create_twitter_account_slug(instance, new_slug=None):
    """
    Creates a new twitter account slug
    """
    slug = slugify(instance.twitter_handle)
    if new_slug is not None:
        slug = new_slug
    qs = TwitterAccount.objects.filter(slug=slug).order_by('id')
    if qs.exists():
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_twitter_account_slug(instance, new_slug=new_slug)
    return slug


def pre_save_twitter_account_receiver(sender, instance, *args, **kwargs):
    """
    Called when a twitter account is saved
    """
    if not instance.slug:
        instance.slug = create_twitter_account_slug(instance)

pre_save.connect(pre_save_twitter_account_receiver, sender=TwitterAccount)

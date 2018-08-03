from django.conf import settings
from django.db import models


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
        return self.title

    def __str__(self):
        return self.title

    # TODO -> Get the slug working
    # def get_absolute_url(self):
    #     return reverse('blog:post-detail', kwargs={'slug':self.slug})

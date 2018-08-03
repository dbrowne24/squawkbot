from django.contrib import admin

from twitter_accounts.models import TwitterAccount

twitter_accounts_models = [
    TwitterAccount
]

admin.site.register(twitter_accounts_models)

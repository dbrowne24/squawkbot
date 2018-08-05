from django import forms

from twitter_accounts.models import TwitterAccount


# TODO -> Shall we have them add their own twitter handle or can we just pull this???
class TwitterAccountForm(forms.ModelForm):
    class Meta:
        model = TwitterAccount
        fields = [
            'twitter_handle',
            'consumer_key',
            'consumer_secret',
            'access_token',
            'access_secret',
        ]

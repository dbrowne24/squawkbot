from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from twitter_accounts.models import TwitterAccount
from twitter_accounts.forms import TwitterAccountForm
from bot_tasks.models import BotTask


class HomeView(ListView):
    """
    The home view should show a list of the users accounts
    """
    model = TwitterAccount
    context_object_name = 'twitter_account_list'
    template_name = 'twitter_accounts/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        # TODO Filter by the user
        queryset = TwitterAccount.objects.all()
        return queryset


class CreateTwitterAccountView(FormView):
    """
    Allows the user to create a twitter account
    """
    template_name = 'twitter_accounts/twitter_account_form.html'
    form_class = TwitterAccountForm
    success_url = '/'

    # TODO -> Is there anything else that we want to do if the form is not valid??
    # TODO Think that I will need to save and commit the form here?? Does it do it itself? probably not
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owned_by = self.request.user
        instance.save()
        messages.success(self.request, 'Your Twitter account has been added successfully')
        return super().form_valid(form)

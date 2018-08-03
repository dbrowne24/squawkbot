from django.urls import path

from twitter_accounts import views

app_name = 'twitter_accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_twitter_account/', views.CreateTwitterAccountView.as_view(), name='add-twitter-account')
]

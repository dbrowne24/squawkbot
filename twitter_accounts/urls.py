from django.urls import path
from twitter_accounts import views

app_name = 'twitter_accounts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_twitter_account/', views.CreateTwitterAccountView.as_view(), name='add-twitter-account'),
    # path('twitter_account/<slug:slug>/', views.TwitterAccountDetail.as_view(), name='twitter-account-detail'),
    path('twitter_account/<slug:slug>/delete/', views.TwitterAccountDelete.as_view(), name='twitter-account-delete')
]

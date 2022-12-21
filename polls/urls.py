from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserDelete

app_name = 'polls'
urlpatterns = [
    path('delete_account/', views.UserDelete.as_view(), name='delete_account'),
    path('update_account/', views.UpdateDate.as_view(), name='update_account'),
    path('personal_account/', views.PersonalAccount.as_view(), name='personal_account'),
    path('', views.IndexView.as_view(), name='home_page'),
    path('/', views.DetailView.as_view(), name='detail'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('vote/', views.vote, name='vote'),
    path('register', views.RegisterUser.as_view(), name='register'),
]
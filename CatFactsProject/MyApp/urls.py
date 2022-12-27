from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('index', views.index, name='index'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
]
"""wsd_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path, include
from store.views import *
from store.game_developer_info import *

urlpatterns = [
    path('admin/', admin.site.urls), # TODO remove later

    path('', index, name="home"),
    path('accounts/edit_profile/', edit_profile),
    path('accounts/logout/', page_logout, name="logout"),
    path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('accounts/my_games', my_games),
    path('games/add/', add_game),

    path('game/<int:game_id>/<str:game_name>', show_game),
    path('payment_error', show_payment_error),
    path('payment_cancelled', show_payment_cancel),

    path('game/<int:game_id>/<str:game_name>/play', play_game),

    path('game/<int:game_id>/<str:game_name>/play/post_score', post_score),
    path('game/<int:game_id>/<str:game_name>/play/save_state', save_state),
    path('game/<int:game_id>/<str:game_name>/play/get_state', get_state),
    path('game/<int:game_id>/<str:game_name>/play/post_settings', post_settings),
]


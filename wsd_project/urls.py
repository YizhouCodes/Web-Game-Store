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
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls import url, include
from store.views import *
from store.game_developer_info import *
from store_rest_api_v1 import urls as api_urls

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/signup/', register, name='register'),
    path('accounts/activate/<uidb64>/<token>/', activate, name='activate'),
    #path('accounts/signup_developer/',views.register_developer),
    path('accounts/password_recovery/', password_recovery, name='password_recovery'),
    path('accounts/reset/<uidb64>/<token>/', reset, name='reset'),
    path('accounts/reset/done/', reset_done, name='reset_done'),
    path('', index, name="home"),
    path('accounts/edit_profile/', edit_profile),
    path('accounts/logout/', page_logout, name="logout"),
    path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('accounts/my_games', my_games),
    path('games/add/', add_game),
    path('game/edit/<int:game_id>/<str:game_name>/', edit_game),

    path('game/<int:game_id>/<str:game_name>', show_game),
    path('game/<int:game_id>/<str:game_name>/add_review', add_review),
    path('payment_error', show_payment_error),
    path('payment_cancelled', show_payment_cancel),
    url(r'^accounts/', include('allauth.urls')),

    path('game/<int:game_id>/<str:game_name>/play', play_game),

    path('game/<int:game_id>/<str:game_name>/play/post_score', post_score),
    path('game/<int:game_id>/<str:game_name>/play/save_state', save_state),
    path('game/<int:game_id>/<str:game_name>/play/get_state', get_state),
    path('game/<int:game_id>/<str:game_name>/play/post_settings', post_settings),

    path('apiv1/', include(api_urls)),
]

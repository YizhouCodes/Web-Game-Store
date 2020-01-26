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
from store.views import edit_profile, index, page_logout, add_game, show_game,show_payment_error, show_payment_cancel
from store.views import register, activate, password_recovery, reset



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', register, name='register'),
    path('accounts/activate/<uidb64>/<token>/', activate, name='activate'),
    #path('accounts/signup_developer/',views.register_developer),
    path('accounts/password_recovery/', password_recovery),
    path('accounts/reset/<uidb64>/<token>/', reset, name='reset'),
    #path('reset/done/', views.password_reset_done),
    path('', index, name="home"),
    path('accounts/edit_profile/', edit_profile),
    path('accounts/logout/', page_logout, name="logout"),
    #path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('games/add/', add_game),

    path('game/<int:game_id>/<str:game_name>', show_game),
    path('payment_error', show_payment_error),
    path('payment_cancelled', show_payment_cancel),

]

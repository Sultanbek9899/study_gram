from django.urls import path

from apps.users.views import LoginView, logout_user

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name="logout"),
]
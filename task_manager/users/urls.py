from django.urls import path
from .views import (UsersView,
                    UserCreateView,
                    UserUpdateView,
                    UserDeleteView)


urlpatterns = [
    path('', UsersView.as_view(), name='home_users'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),
]

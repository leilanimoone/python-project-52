from django.urls import path
from .views import (TasksListView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView,
                    TaskDetailView)


urlpatterns = [
    path('', TasksListView.as_view(), name='home_tasks'),
    path('<int:pk>/', TaskDetailView.as_view(), name='view_task'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
]

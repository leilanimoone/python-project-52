from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from .views import SignIn, LogOut


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('login/', SignIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls',)),
    path('statuses/', include('task_manager.statuses.urls',)),
    path('tasks/', include('task_manager.tasks.urls',)),
    path('labels/', include('task_manager.labels.urls',)),
]

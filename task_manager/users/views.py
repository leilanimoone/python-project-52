from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CheckMixin
from .forms import UserForm
from .models import User


class UsersView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/user.html'
    extra_context = {'title': _('Users')}


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'users/create_user.html'
    extra_context = {'title': _('Create user')}
    success_message = _('User created successfully')


class UserUpdateView(CheckMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('home_users')
    success_message = _('User successfully changed')


class UserDeleteView(CheckMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('home_users')
    success_message = _('User successfully deleted')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('home_users')

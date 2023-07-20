from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .statuses.models import Statuses
from .tasks.models import Tasks
from .labels.models import Labels


class CheckMixin:
    def has_permission(self) -> bool:
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                messages.error(self.request, _('You are not authorized!'))
            )
            return redirect('login')
        elif not self.has_permission():
            messages.error(
                request,
                messages.error(self.request, _("You have't permission!"))
            )
            return redirect('home_users')
        return super().dispatch(request, *args, **kwargs)


class StatusMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Statuses
    extra_context = {'title': _('Statuses'), 'button': _('Create')}
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home_statuses')
    fields = ['name']


class TasksMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Tasks
    extra_context = {'title': _('New Tasks'), 'button': _('Create')}
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home_tasks')
    fields = ['name', 'description', 'status', 'executor', 'labels']


class LabelsMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Labels
    extra_context = {'title': _('Labels'), 'button': _('Create')}
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home_labels')
    fields = ['name']
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .statuses.models import Statuses
from .tasks.models import Tasks
from .labels.models import Labels


class CheckMixin:
    def has_permission(self):
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


class DeleteProtectionMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)


class StatusMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Statuses
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home_statuses')
    fields = ['name']


class TasksMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Tasks
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home_tasks')
    fields = ['name', 'description', 'status', 'executor', 'labels']


class LabelsMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Labels
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home_labels')
    fields = ['name']

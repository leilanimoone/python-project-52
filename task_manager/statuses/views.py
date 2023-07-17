from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import StatusMixin


class StatusesListView(StatusMixin, ListView):
    context_object_name = 'statuses'


class StatusCreateView(StatusMixin, CreateView):
    success_message = _("Status created successfully")
    template_name = 'form.html'


class StatusUpdateView(StatusMixin, UpdateView):
    success_message = _('Status successfully changed')
    template_name = 'form.html'
    extra_context = {'title': _('Statuses'), 'button': _('Change')}


class StatusDeleteView(StatusMixin, DeleteView):
    template_name = 'delete_form.html'

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(
                self.request,
                _('Status successfully deleted')
            )
            return redirect(reverse_lazy('home_statuses'))
        except ProtectedError:
            messages.error(
                self.request,
                _("Error! Can't delete, status in use")
            )
            return redirect(reverse_lazy('home_statuses'))

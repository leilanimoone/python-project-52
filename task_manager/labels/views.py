from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import LabelsMixin


class LabelsListView(LabelsMixin, ListView):
    context_object_name = 'labels'
    template_name = 'labels/labels.html'


class LabelCreateView(LabelsMixin, CreateView):
    success_message = _("Label created successfully")
    template_name = 'form.html'


class LabelUpdateView(LabelsMixin, UpdateView):
    success_message = _('Label successfully changed')
    template_name = 'form.html'
    extra_context = {'title': _('Labels'), 'button': _('Change')}


class LabelDeleteView(LabelsMixin, DeleteView):
    template_name = 'delete_form.html'

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(
                self.request,
                _('Label successfully deleted')
            )
            return redirect(reverse_lazy('home_labels'))
        except ProtectedError:
            messages.error(
                self.request,
                _("Error! Can't delete, label in use")
            )
            return redirect(reverse_lazy('home_labels'))

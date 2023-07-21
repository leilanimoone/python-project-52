from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.shortcuts import redirect
from django_filters.views import FilterView
from .filters import TaskFilter
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import TasksMixin


class TasksListView(TasksMixin, FilterView):
    context_object_name = 'tasks'
    template_name = 'tasks/tasks.html'
    filterset_class = TaskFilter
    extra_context = {'title': _('Tasks'), 'button': _('Show')}


class TaskCreateView(TasksMixin, CreateView):
    template_name = 'form.html'
    success_message = _("Task created successfully")
    extra_context = {'title': _('Create task'), 'button': _('Create')}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDetailView(TasksMixin, DetailView):
    context_object_name = 'task'
    template_name = 'tasks/tasks_show.html'
    extra_context = {'title': _('Show task')}


class TaskUpdateView(TasksMixin, UpdateView):
    template_name = 'form.html'
    extra_context = {'title': _('Update task'), 'button': _('Change')}
    success_message = _('Task successfully changed')


class TaskDeleteView(TasksMixin, DeleteView):
    template_name = 'delete_form.html'
    success_message = _('Task successfully deleted')
    extra_context = {'title': _('Delete task'), 'button': _('Yes, delete')}

    def has_permission(self) -> bool:
        return self.get_object().author.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                _("Error! You are not authenticated")
            )
            return self.handle_no_permission()

        elif not self.has_permission():
            messages.error(
                request,
                _("Error! You can't delete this task. Only author")
            )
            return redirect('home_tasks')
        return super().dispatch(request, *args, **kwargs)

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode

from issue_tracker.forms.form_task import TaskForm
from issue_tracker.models import Task

from issue_tracker.forms.search_forms import SearchForm


class IndexView(ListView):
    template_name = 'index.html'

    model = Task
    context_object_name = 'tasks'
    ordering = ('created_at',)
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(project__name__icontains=self.search_value) | \
                    Q(status__name__icontains=self.search_value) | Q(type__name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


class CreateTask(CreateView):
    template_name = 'add_task.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDetail(DetailView):
    template_name = 'task_detail.html'
    model = Task


class TaskUpdate(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = TaskForm(instance=context['task'])
        return context

    def post(self, request: WSGIRequest, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, 'task_update.html', context={'form': form, 'task': task})


class DeleteTask(DeleteView):
    template_name = 'task_detail.html'
    model = Task
    context_object_name = 'task'
    extra_context = {'delete': 'delete'}
    success_url = reverse_lazy('index')

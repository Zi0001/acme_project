
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday
    template_name_suffix = '_detail'

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        # Возвращаем словарь контекста.
        return context

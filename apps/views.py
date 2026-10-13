from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.forms import TodoModelForm
from apps.models import Todo


class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = "todos"
    paginate_by = 6
    ordering = ["is_done", "-created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        status = self.request.GET.get("status", "")

        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if status == "done":
            queryset = queryset.filter(is_done=True)
        elif status == "active":
            queryset = queryset.filter(is_done=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get("q", "").strip()
        status = self.request.GET.get("status", "")

        total = Todo.objects.count()
        done_count = Todo.objects.filter(is_done=True).count()

        context["q"] = q
        context["status"] = status
        context["total"] = total
        context["done_count"] = done_count
        context["active_count"] = total - done_count
        # Sahifalash havolalarida qidiruv va filtr saqlanib qolishi uchun
        context["extra_query"] = urlencode({k: v for k, v in (("q", q), ("status", status)) if v})
        return context


class TodoCreateView(SuccessMessageMixin, CreateView):
    model = Todo
    form_class = TodoModelForm
    template_name = "todo_form.html"
    success_url = reverse_lazy("home")
    success_message = "Vazifa muvaffaqiyatli qo'shildi!"


class TodoUpdateView(SuccessMessageMixin, UpdateView):
    model = Todo
    form_class = TodoModelForm
    template_name = "todo_form.html"
    success_url = reverse_lazy("home")
    success_message = "Vazifa yangilandi!"


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_confirm_delete.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        title = self.object.title
        response = super().form_valid(form)
        messages.success(self.request, f"“{title}” o'chirildi.")
        return response

from django.urls import path

from apps.views import TodoCreateView, TodoDeleteView, TodoListView, TodoUpdateView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("todo/create/", TodoCreateView.as_view(), name="todo_create"),
    path("todo/<int:pk>/update/", TodoUpdateView.as_view(), name="todo_update"),
    path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
]

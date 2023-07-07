from django.urls import include, path
from . import views

app_name = 'main'

urlpatterns = [
    path('todos/', views.TodoListView.as_view(), name='todos'),
    path('todos/<pk>', views.DetailTodo.as_view(), name='detail'),
    path('create/', views.CreateTodo.as_view(), name='create'),
    path('delete/<pk>', views.DeleteTodo.as_view(), name='delete'),
]
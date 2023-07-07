
from rest_framework import generics 
from rest_framework.response import Response
from .serializers import ToDoSerializer
from .models import Todo

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer



class TaskViewSet(APIView):

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
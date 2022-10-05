from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Task
from .serializers import TasksSerializer



class TaskViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for Tasks.
    """

    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [
      DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
    ]
    filterset_fields = ("title", "user", "is_complete")
    search_fields = ("title", "subject")
    ordering_fields = ("is_complete", "created_at", "updated_at", "deadline")
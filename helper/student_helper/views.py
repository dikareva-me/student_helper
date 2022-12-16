from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TasksSerializer



class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TasksSerializer
    queryset = Task.objects.all()
    filter_backends = [
      DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
    ]
    filterset_fields = ("title", "user", "is_complete")
    search_fields = ("title", "subject")
    ordering_fields = ("is_complete", "created_at", "updated_at", "deadline")
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



    

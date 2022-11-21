from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TasksSerializer

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status



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
  #  queryset = Task.objects.all()
  # serializer_class = TasksSerializer
  #  permission_classes = [IsAuthenticated]

   # def get(self, request):
   #     user_id = request.get("user")
    #    print(self.request.user.username)
     #   if request.user.is_authenticated():
      #    return self.queryset.filter(user=request.user.username)
       
    


  #  queryset = Task.objects.all()
  #  serializer_class = TasksSerializer
   # filter_backends = [
    #  DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,
  #  ]
   # filterset_fields = ("title", "user", "is_complete")
   # search_fields = ("title", "subject")
   # ordering_fields = ("is_complete", "created_at", "updated_at", "deadline")
   # permission_classes = [IsAuthenticated]
   

    

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer    

    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


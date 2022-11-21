from rest_framework.routers import DefaultRouter
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views

router = DefaultRouter()
router.register("api/task", views.TaskViewSet, basename="task")

urlpatterns = [
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
#    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
 #   path('update_profile/<int:pk>/', views.UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),

]
urlpatterns += router.urls
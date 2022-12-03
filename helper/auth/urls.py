from django.urls import path
from auth.views import RegisterView, ChangePasswordView, ChangeProfileView, UserView

from knox import views as knox_views
from .views import LoginAPI
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'), 
    path('change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/', ChangeProfileView.as_view(), name='auth_update_profile'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/', UserView.as_view(), name='user_info')

]
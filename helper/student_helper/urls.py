from rest_framework.routers import DefaultRouter
from django.urls import path


from . import views

router = DefaultRouter()
router.register("api/task", views.TaskViewSet, basename="task")


urlpatterns = router.urls
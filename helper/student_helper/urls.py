from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("api/task", views.TaskViewSet, basename="task")
urlpatterns = router.urls
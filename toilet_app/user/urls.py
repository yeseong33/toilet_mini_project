from rest_framework.routers import DefaultRouter
from . import views

app_name = "user"
router = DefaultRouter()
router.register("", views.UsersView)

urlpatterns = router.urls
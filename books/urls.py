from django.urls import path, include
from books import views
from rest_framework.routers import SimpleRouter
from .views import userviewset, bookviewset, reservesviewset

router = SimpleRouter()
router.register('user', userviewset)
router.register('book', bookviewset)
router.register('reserve', reservesviewset)
urlpatterns = router.urls

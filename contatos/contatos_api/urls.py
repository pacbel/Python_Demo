from rest_framework.routers import DefaultRouter

from .views import ContactViewSet

router = DefaultRouter()
router.register('contatos', ContactViewSet, basename='contato')

urlpatterns = router.urls

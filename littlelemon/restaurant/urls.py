from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register('menu', MenuViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = router.urls

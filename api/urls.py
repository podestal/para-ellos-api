from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('customers', views.CustomerViewSet)
router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)
router.register('orders', views.OrderViewSet)
router.register('orderItems', views.OrderItemSerializer)
router.register('carts', views.CartViewSet)
router.register('cartItems', views.CartItemViewSet)

urlpatterns = router.urls
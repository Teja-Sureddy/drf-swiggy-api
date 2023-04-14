from django.urls import path, include
from .views.user import UserViewSet
from .views.role import RoleViewSet
from .views.restaurant import RestaurantViewSet
from .views.menu import MenuViewSet
from .views.order import OrderViewSet
from .views.ordered_items import OrderedItemsViewSet
from .views.auth_token import CustomAuthToken
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'roles', RoleViewSet, basename="role")
router.register(r'restaurants', RestaurantViewSet, basename="restaurant")
router.register(r'menus', MenuViewSet, basename="menu")
router.register(r'orders', OrderViewSet, basename="order")
router.register(r'orderedItems', OrderedItemsViewSet, basename="orderedItem")

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth')
]

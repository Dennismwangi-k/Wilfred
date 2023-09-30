from django.urls import path
from rest_framework import routers
from user.views import WasteCollectorViewSet
from .views import DeliveryListView
from .views import DeliveryDetailView
from .views import MessageListView
from .views import MessageDetailView
from .views import LocationListView
from .views import LocationDetailView
from .views import OrderItemListView
from .views import OrderItemDetailView
from .views import ProductListView
from .views import ProductDetailView
from .views import CategoryListView
from .views import CategoryDetailView
from django.urls import path, include
from rest_framework import routers
from .views import OrderListView
from .views import OrderDetailView
from .views import UserViewSet 

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("registerwastecollector", WasteCollectorViewSet, basename="register-wastecollector")
urlpatterns = [
    path('delivery/', DeliveryListView.as_view(), name='Delivery_list_view'),
    path('delivery/<int:id>/', DeliveryDetailView.as_view(), name='Delivery_detail_view'),
    path('message/', MessageListView.as_view(), name='Message_list_view'),
    path('message/<int:id>/', MessageDetailView.as_view(), name='Message_detail_view'),
    path('location/', LocationListView.as_view(), name='Location_list_view'),
    path('location/<int:id>/', LocationDetailView.as_view(), name='Location_detail_view'),
    path('orderItem/', OrderItemListView.as_view(), name='OrderItem_list_view'),
    path('orderItem/<int:id>/', OrderItemDetailView.as_view(), name='OrderItem_detail_view'),
    path('product/', ProductListView.as_view(), name='product-list-create'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product-list-create'),
    path('category/', CategoryListView.as_view(), name='category-list-create'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-list-create'),
    path('order/', OrderListView.as_view(), name='order-list-create'),
    path('order/<int:id>/', OrderDetailView.as_view(), name='order-list-create'),
    path('api/', include(router.urls)),  

]



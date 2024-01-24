from django.urls import path, include
from rest_framework.routers import DefaultRouter

#import de views
from .saleView import SaleViewSet, SaleListView
from .clientView import ClientViewset, ClientListView
from .productView import ProductViewset

# Create router
router = DefaultRouter()

# Register the viewsets 
router.register(r'sales', SaleViewSet, basename='sale')
router.register(r'clients', ClientViewset, basename='client')
router.register(r'products', ProductViewset, basename='product')



urlpatterns = [
    
    # Incluye las rutas generadas por el enrutador
    path('api/', include(router.urls)),
    path('api/sales-list/', SaleListView.as_view(), name='sales-list'),
    path('api/clients-list/', ClientListView.as_view(), name='client-list'),
]

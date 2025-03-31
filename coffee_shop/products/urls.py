from django.urls import path
from .views import ProductDetailView, ProductFormView, ProductListView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Ruta para la página de inicio
    path('productos/', ProductListView.as_view(), name="list_product"),
    path('agregar/', ProductFormView.as_view(), name="add_product"),
    path('producto/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),  # Detalles de un producto
]

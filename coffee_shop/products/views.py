from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Product
from django.views.generic import TemplateView
from django.views.generic import DetailView





# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"  # Especificamos la plantilla para esta vista

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"  # La plantilla que se utilizará para mostrar el detalle
    context_object_name = "product"  # El nombre del objeto que estará disponible en el contexto

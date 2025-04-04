from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Product
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from .forms import ContactForm


from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render



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


class HomeView(TemplateView):
    template_name = "home.html"  # Especificamos la plantilla para esta vista

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"  # La plantilla que se utilizará para mostrar el detalle
    context_object_name = "product"  # El nombre del objeto que estará disponible en el contexto

class ContactView(FormView):
    template_name = "contact.html"  # La plantilla que se usará
    form_class = ContactForm  # Usamos el formulario que creamos
    success_url = reverse_lazy("home")  # Redirige a la página de inicio después de enviar el formulario

    def form_valid(self, form):
         # Obtenemos los datos del formulario
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Componer el mensaje
        subject = f"Nuevo mensaje de contacto de {name}"
        message_body = f"Has recibido un mensaje de {name} ({email}):\n\n{message}"
        from_email = settings.EMAIL_HOST_USER  # El correo que usas para enviar el mensaje
        recipient_list = ['jimyymij28@gmail.com']  # El correo de la tienda donde se recibe el mensaje

        # Enviar el correo
        send_mail(subject, message_body, from_email, recipient_list)

        # Redirigimos al usuario a la página de inicio
        return super().form_valid(form)
    


from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from products.models import Product
from comments.forms import CommentForm
from django.conf import settings
import stripe
# Create your views here.

class TestView(TemplateView):
    template_name = "products/test.html"


class HomeView(TemplateView):
    template_name = "products/index.html"

    def get_context_data(self,*args,**kwargs):
        products = Product.objects.all()
        return {'products':products}
    

class ProductoDetailView(DetailView):
    model = Product
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context
    

class ProductBuyView(DetailView):
    model = Product
    template_name = 'products/buy.html'

    def post(self,request,*args,**kwargs):
        stripe.api_key = settings.STRIPE_API_KEY
        token = request.POST['stripeToken']
        product = self.get_object()

        charge = stripe.Charge.create(
            amount = product.price,
            currency = 'usd',
            description = "cobro por {}".format(product.title),
            statement_descriptor = 'cobro platzicomerce',
            source = token,
        )
        return render(request,"products/succes.html",{'debug_info': charge, 'product':product})

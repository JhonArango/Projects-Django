from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

#  Este mixin requerira que el usuario sea miembro del staff,
#  Un mixin son una o varias funcionalidades para una clase 
#  podemos crearla una vez y heredar su comportamiento donde 
#  queramos dandole prioridad a su implementacion antes que a la otra clase
class StaffRequiredMixin(object):
    # me permite identificar si el usuario es miembro del staff si no lo es me redirecciona a login.
     @method_decorator(staff_member_required)
     def dispatch(self,request, *args, ** kwargs):
        # Este if ya no es necesario al utilizar el decorator con el requerimiento.
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin,self).dispatch(request, *args, ** kwargs)

# Create your views here.
class PageListView(ListView):
    model=Page

class PageDetailView(DetailView):
    model=Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url= reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    success_url= reverse_lazy('pages:pages')

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


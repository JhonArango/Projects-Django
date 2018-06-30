from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    # mostrar si es peticion GET o POST
    # print("Tipo de peticion: {}" .format(request.method))
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo y dreccionamos
            email = EmailMessage(
                "La cafeteria: nuevo mensaje contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["jhonarang.93@utp.edu.co"],
                reply_to=[email]
            )
            try:
                email.send()
                 # Todo bien
                return redirect(reverse('contact')+"?ok")
            except:
                # algo fallo
                return redirect(reverse('contact')+"?fail")


    return render(request,"contact/contact.html",{'form':contact_form})
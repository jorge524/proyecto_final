from django.shortcuts import render, redirect
from django.urls import reverse
from . import views 
from .forms import ContactoForm
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    print("Tipo de peticion: {}".format(request.method))
    contacto_form=ContactoForm() #intanciamos el formulario
    if request.method == "POST":
        contacto_form=ContactoForm(data=request.POST)
        if contacto_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            #enviar correo y direcionar
            email=EmailMessage(
                "ITQ: Nuevo Mensaje de contacto",
                "De {} <{}>\n\nEsbribio:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["jramon406@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contacto')+"?ok")
            except:
                return redirect(reverse('contacto')+"?Error")

            

    return render(request, "contacto/contacto.html", {'form': contacto_form})


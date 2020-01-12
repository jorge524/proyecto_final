from django.shortcuts import render, HttpResponse

# Create your views here.
html_cabecera="""
<h1>Mi primera Web </h1><h2>Inicio</h1> 
<ul>
    <li><a href="/">Inicio </a></li>
    <li><a href="/presentacion">presentacion </a>algo de mi</li>
    <li><a href="/catalogo">catalogo </a>catalogo</li>
    <li><a href="/contacto">contacto </a>contacto</li>
</ul>
"""
    
def home(request):
    return render (request,"core/home.html")

def presentacion(request):
    return render (request,"core/presentacion.html")


def catalogo(request):
    return render (request,"core/catalogo.html")

def contacto(request):
    return render (request,"core/contacto.html")






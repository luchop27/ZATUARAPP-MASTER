from itertools import product

from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from Blogs.models import *
from Clientes.models import *
from Home.models import *
from django.shortcuts import *

from Productos.models import *

def index(request):
    contexto = {
        "sliders": Slider.objects.all().order_by("orden"),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
        'personalizacion': Personalizaion_Poducto.objects.all(),
        'proceso': Proceso.objects.all().first(),
        'galeri_proces': Galeria_Proceso.objects.all(),
        'catalogo': Descarga.objects.all().first(),
        'identidad': Identidad.objects.all(),
        'detalles': Detalles.objects.first(),
        'linea' : Linea_Product.objects.all().order_by('-id'),
        'clientes': Cliente.objects.all(),
    }
    return render(request,"index.html",contexto)

def empresa(request):
    contexto={
        'zatuar': Zatuar_marca.objects.all().first(),
        'beneficio':Beneficios.objects.all(),
        'proceso': Proceso.objects.all().first(),
        'contacto':Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    return render(request,"empresa.html",contexto)

def linea(request):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.all().order_by('-id'),
        'producto_personalizacion':Producto_Personalizacion.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
        'linea': Linea_Product.objects.all(),
    }
    return render(request,"productos.html", contexto)

def linea_cate(request, lineaa):
    contexto = {
        'clasif_producto': Clasif_producto.objects.filter(linea__linea=lineaa),
        'product': Product.objects.filter(clasif__linea__linea=lineaa),
        # 'product': Product.objects.all().order_by('-id'),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'linea': Linea_Product.objects.all(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'productos.html', contexto,)

def producto(request):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.all().order_by('-id'),
        'producto_personalizacion':Producto_Personalizacion.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
        'linea': Linea_Product.objects.all(),
    }
    return render(request,"productos.html", contexto)


def producto_cate(request, id):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.filter(clasif_id=id),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'linea': Linea_Product.objects.all(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'productos.html', contexto,)


def producto_id(request, id):
    contexto = {
        'clasif_producto': Clasif_producto.objects.all(),
        'product': Product.objects.get(id=id),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'product.html', contexto,)

def clientes(request):
    contexto={
        'client':Cliente.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }
    return render(request, 'clientes.html', contexto)

def clientes_id(request,id):
    client=Cliente.objects.get(id=id)
    galeria_cliente=Galeria_Cliente.objects.filter(cliente=client)
    zatuar=Zatuar_marca.objects.get()
    contacto=Contacto_empresa.objects.all().first()
    redes= Redes_sociales.objects.all().first()
    return render(request,'product-client.html',
                              {'client': client,
                               'galeria_cliente':galeria_cliente,
                               'zatuar':zatuar,
                               'contacto':contacto,
                               'redes':redes,
                      })

def blog(request):
    contexto = {
        'visitas': Visitas_Blog.objects.all(),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),

    }

    return render(request,"blog-large-image-sidebar-right.html", contexto)




def post(request, n):
    try:
        Visitas_Blog(blog_id=n).save()

    except:
        visita = Visitas_Blog.objects.get(blog_id=n)
        visita.save()
    contexto = {
        'blogg': Blogs.objects.get(id=n),
        'blogs': Blogs.objects.all(),
        'categorias': Categoria.objects.all(),
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    return render(request, "blog-post-sidebar-right.html", contexto)



def error404(request):
    return render(request,"page-404.html")

def contacto(request):
    contexto = {
        'zatuar': Zatuar_marca.objects.all().first(),
        'contacto': Contacto_empresa.objects.all().first(),
        'redes': Redes_sociales.objects.all().first(),
    }
    if request.POST:
        enviar_email(request,request.POST['subject'],request.POST['email'],"zatuar.ec@gmail.com",request.POST['message'],request.POST['name'])
    return render(request,'contact-us.html',contexto)



def enviar_email(request,asunto,from_email,to,mensaje,nombre):
    asunto = asunto
    from_email = from_email
    to = to
    text_content = 'Este mnsaje es importante.'
    html_content = '<p>This is an <strong>important</strong> message.</p>' \
                   '<img src="http://zatuar.com/static/img/zatuar/favizatuar.png"><br>' + mensaje
    msg = EmailMultiAlternatives(asunto, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # print from_email





from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from app_final.models import Usuario, Review, Juego
from app_final.forms import Usuario_formulario, Review_formulario, Juego_formulario, Buscar_por_autor, Buscar_por_juego
# Create your views here.


def inicio(request):
    return render(request, "app_final/inicio.html")

def registrar_usuario(request):
    if request.method == 'POST':
        formulario_registro_usuario = Usuario_formulario(request.POST)

        
        print(formulario_registro_usuario)
        if formulario_registro_usuario.is_valid:
            
            informacion_usuario = formulario_registro_usuario.cleaned_data

            #Me fijo que el nombre de usuario no exista con anterioridad
            usuarios_existentes = Usuario.objects
            existe = False
            for usuarios in usuarios_existentes.all():
                if usuarios.nombre_usuario == informacion_usuario['nombre_usuario']:
                    existe = True
            if existe:
                return render(request, "app_final/usuario_ya_existe.html")
            else:
                usuario = Usuario(nombre_usuario = informacion_usuario['nombre_usuario'], email_usuario = informacion_usuario['email_usuario'])

                usuario.save()

                return render(request, "app_final/inicio.html")

    else:

        formulario_registro_usuario = Usuario_formulario()
        
        return render(request, "app_final/registrar_usuario.html", {"formulario_registro_usuario":formulario_registro_usuario})

    

def agregar_juego(request):
    if request.method == 'POST':
        formulario_registro_juego = Juego_formulario(request.POST)

        
        print(formulario_registro_juego)
        if formulario_registro_juego.is_valid:
            
            informacion_juego = formulario_registro_juego.cleaned_data
            #Me fijo que el juego no exista ya en la DB
            juegos_existentes = Juego.objects
            existe = False
            for juegos in juegos_existentes.all():
                if juegos.nombre_juego == informacion_juego['nombre_juego']:
                    existe = True
            
            if existe:
                return render(request, "app_final/juego_ya_existe.html")
            else:
                juego = Juego(nombre_juego = informacion_juego['nombre_juego'], genero_juego = informacion_juego['genero_juego'], desarrollador = informacion_juego['desarrollador'])

                juego.save()

                return render(request, "app_final/inicio.html")

    else:

        formulario_registro_juego = Juego_formulario()
        
        return render(request, "app_final/agregar_juego.html", {"formulario_registro_juego":formulario_registro_juego})



def crear_review(request):
    if request.method == 'POST':
        formulario_review = Review_formulario(request.POST)

        
        print(formulario_review)
        if formulario_review.is_valid:
            
            informacion_review = formulario_review.cleaned_data
            #El juego debe estar en mi base de datos para ingresar la review
            juegos_existentes = Juego.objects
            existe = False
            for juegos in juegos_existentes.all():
                if juegos.nombre_juego == informacion_review['juego_review']:
                    existe = True
            
            if existe:

                #El usuario debe haber ingresado un nombre de usuario existente, o anonimo
                usuarios_existentes = Usuario.objects
                existe = False
                for usuarios in usuarios_existentes.all():
                    if usuarios.nombre_usuario == informacion_review['nombre_autor']:
                        existe = True
                if "anonimo" == informacion_review['nombre_autor']:
                    existe = True
                if existe:
                    review = Review(nombre_autor = informacion_review['nombre_autor'], titulo_review = informacion_review['titulo_review'], contenido_review = informacion_review['contenido_review'], puntaje_review = informacion_review['puntaje_review'], juego_review = informacion_review['juego_review'])

                    review.save()

                    return render(request, "app_final/inicio.html")

                else:
                    return render(request, "app_final/usuario_incorrecto.html")
                
            else:
                return render(request, "app_final/juego_no_existe.html")

    else:

        formulario_review = Review_formulario()
        
        return render(request, "app_final/crear_review.html", {"formulario_review":formulario_review})



def ver_todo(request):
    juegos = Juego.objects.all()
    reviews = Review.objects.all()
    return render(request, "app_final/ver_todo.html", {"juegos":juegos, "reviews":reviews})

def ver_por_juego(request):
    formulario_busqueda = Buscar_por_juego()
    return render(request, "app_final/ver_por_juego.html", {"formulario_busqueda":formulario_busqueda})

def ver_por_juego_resultado(request):
    
    if request.GET['nombre_juego']:
        nombre_juego = request.GET['nombre_juego']
        juegos = Juego.objects.filter(nombre_juego__icontains=nombre_juego)
        reviews = Review.objects.all()

        return render(request, "app_final/ver_por_juego_resultado.html", {"reviews":reviews, "juegos":juegos, "nombre_juego":nombre_juego})

    else:
       
        return render(request, "app_final/inicio.html")

def ver_por_usuario(request):
    formulario_busqueda = Buscar_por_autor()
    return render(request, "app_final/ver_por_usuario.html", {"formulario_busqueda":formulario_busqueda})

def ver_por_usuario_resultado(request):
    if request.GET["nombre_autor"]:
        nombre_autor = request.GET["nombre_autor"]
        juegos = Juego.objects.all()
        reviews = Review.objects.filter(nombre_autor__icontains=nombre_autor)
        return render(request, "app_final/ver_por_usuario_resultado.html", {"juegos":juegos, "reviews":reviews, "nombre_autor":nombre_autor})

    else:
        return render(request, "app_final/inicio.html")
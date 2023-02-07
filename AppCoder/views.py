from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *

# Create your views here.

def inicio(request):

    return render(request,"AppCoder/inicio.html")

def curso(request):

    if request.method == "POST":    #despues de dar el botón enviar
            
            formulario1 = CursoFormulario(request.POST)

            if formulario1.is_valid():
                info = formulario1.cleaned_data

                curso = Curso(nombre=info["curso"],camada = info["camada"])
        
                curso.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario1 = CursoFormulario()

    return render(request,"AppCoder/cursos.html",{"form1":formulario1})


def estudiante(request):

    if request.method == "POST":    #despues de dar el botón enviar
            
            formulario2 = EstudianteFormulario(request.POST)

            if formulario2.is_valid():
                info = formulario2.cleaned_data

                estudiante = Estudiante(nombre=info["nombre"],apellido = info["apellido"], correo = info["correo"])
        
                estudiante.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario2 = EstudianteFormulario()

    return render(request,"AppCoder/estudiantes.html",{"form2":formulario2})


def profesor(request):

    if request.method == "POST":    #despues de dar el botón enviar
            
            formulario3 = ProfesorFormulario(request.POST)

            if formulario3.is_valid():
                info = formulario3.cleaned_data

                profe = Profesor(nombre=info["nombre"],apellido = info["apellido"], email = info["email"],profesion = info["profesion"])
        
                profe.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario3 = ProfesorFormulario()

    return render(request,"AppCoder/profesores.html",{"form3":formulario3})

  

def entregable(request):

    if request.method == "POST":    #despues de dar el botón enviar
            
            formulario4 = EntregableFormulario(request.POST)

            if formulario4.is_valid():
                info = formulario4.cleaned_data

                entregable = Entregable(nombre=info["nombre"],fechaEntrega = info["fechaEntrega"])
        
                entregable.save()

                return render(request, "AppCoder/inicio.html")

    else:

            formulario4 = EntregableFormulario()

    return render(request,"AppCoder/entregables.html",{"form4":formulario4})

    
"""
def cursoFormulario(request):

    if request.method == "POST":    #despues de dar el botón enviar
        
        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data

            curso = Curso(nombre=info["curso"],camada = info["camada"])
     
            curso.save()

            return render(request, "AppCoder/cursos.html")

    else:

        formulario1 = CursoFormulario()


    return render(request,"AppCoder/cursos.html",{"form1":formulario1})
"""


def busquedaCamada(request):


    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["camada"]:

       camada = request.GET["camada"] 
       cursos = Curso.objects.filter(camada__iexact=camada)

       return render(request, "AppCoder/inicio.html",{"cursos": cursos, "camada":camada})
    
    else:

        respuesta = "No has enviado datos."


    return render(request, "AppCoder/inicio.html", {"resp1":respuesta})



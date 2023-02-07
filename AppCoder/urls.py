from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio,name="Inicio"),
    path("curso/",curso, name ="Curso"),
    path("profesores/",profesor, name="Profesores"),
    path("estudiantes/",estudiante, name="Estudiantes" ),
    path("entregables/",entregable, name = "Entregables"),
    #path("cursoFormulario/", cursoFormulario, name = "FormularioCurso"),
    path("buscarCamada/",busquedaCamada, name= "BuscarCamada"),
    path("resultados/",resultados, name= "ResultadosBusqueda"),
    ]

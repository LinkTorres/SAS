# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from forms import *
from models import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json

def inicio(request):

    formulario = InicioForm()
    error = []
    if not request.user.is_anonymous(): 
        error.append("Entraste con exito")
        return HttpResponseRedirect("profesor_main/")

    if request.method == "POST":
        formulario = InicioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data["usuario"]
            password = formulario.cleaned_data["password"]
            acceso = authenticate(username=str(usuario), password=str(password))
            if acceso is not None:          
                if acceso.is_active:
                    login(request, acceso)
                    usuario = request.user
                    return HttpResponseRedirect(reverse('inicio'))
                else:
                    error.append("Tu usuario esta desactivado")     
            else:
                error.append('Usuario o contraseña incorrecta')
        else:
            error.append('Usuario o contraseña incorrecta')
    return render(request, 'login.html',locals())

@login_required(login_url='/inicio')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')



@login_required(login_url='/inicio')
def profesor_main(request):
    usuario=request.user
    clave=str(usuario.clave)
    empleado = EmpleadoEscolar.objects.get(cve_usuario__clave=clave)
    profesor = Profesor.objects.get(cve_usuario__cve_usuario__clave=clave)
    return render_to_response('profesor/main.html',locals(),context_instance=RequestContext(request))

def profesor_miperfil(request):
    return render_to_response('profesor/mi-perfil.html',context_instance=RequestContext(request))

def profesor_preferencias(request):
    return render_to_response('profesor/preferencias.html',context_instance=RequestContext(request))

def profesor_logout(request):
    return render_to_response('profesor/logout.html',context_instance=RequestContext(request))

def profesor_mis_grupos(request):
    return render_to_response('profesor/mis-grupos.html',context_instance=RequestContext(request))

def profesor_registrar_calificaciones(request):
    grupolist = ProfesorDaClaseEnGrupo.objects.filter(cve_prof='1002')
    return render_to_response('profesor/registrar-calificaciones.html',locals(),context_instance=RequestContext(request))

def directorio(request):
    profesoresList= Profesor.objects.all()
    materiasList= Materia.objects.all()
    gruposList= Grupo.objects.all()
    return render_to_response('directorio.html',locals(),context_instance=RequestContext(request))

def profesor_reportes_PRUI08_1(request):
    return render_to_response('profesor/reportes/PRUI08.1.html',context_instance=RequestContext(request))

def profesor_reportes_PRUI08_2(request):
    return render_to_response('profesor/reportes/PRUI08.2.html',context_instance=RequestContext(request))

def profesor_calendario(request):
    return render_to_response('profesor/calendario.html',context_instance=RequestContext(request))

def profesor_tutorias(request):
    return render_to_response('profesor/tutorias.html',context_instance=RequestContext(request))

def profesor_ingresa_calificacion(request):
    return render_to_response('profesor/IngresaCalificacion.html',context_instance=RequestContext(request))

def perfiles_profesor(request):
    return render_to_response('perfiles/maldonadoCastilloIdalia.html',context_instance=RequestContext(request))

def perfiles_materia(request):
    return render_to_response('perfiles/ingenieria-de-software.html',context_instance=RequestContext(request))

def perfiles_grupo(request):
    return render_to_response('perfiles/3CM5.html',context_instance=RequestContext(request))   

def profesor_tutorias_comentar(request):
    return render_to_response('profesor/comentar-tutoria.html',context_instance=RequestContext(request))

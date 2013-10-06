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
import reportlab
from reportlab.pdfgen import canvas


def inicio(request):

    usuario = request.user
    formulario = InicioForm()
    error = []
    if not request.user.is_anonymous():

        if usuario.clasificacion ==  'Alumnos':
            return HttpResponseRedirect("alumno/")
        elif usuario.clasificacion ==  'Profesores':
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

def pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def color(materia):
    if(materia.materia.clasificacion=='Institucional'):
        return 'm1'

    elif(materia.materia.clasificacion=='Cientifica_basica'):
        return 'm4'

    elif(materia.materia.clasificacion=='Profesional'):
        return 'm3'

    elif(materia.materia.clasificacion=='Terminal_integración'):
        return 'm2'
    else:
        return 'm3'


def profesor_main(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    Materias=MateriaImpartidaEnGrupo.objects.filter(profesor__cve_usuario__clave=profesor)
    for materia in Materias:

        if(materia.horario.cve_horario==1):
            materia1=materia.materia.nombre
            m1=color(materia)
            grupo1=materia.grupo
        elif(materia.horario.cve_horario==2):
            materia2=materia.materia.nombre
            m2=color(materia)
            grupo2=materia.grupo
        elif(materia.horario.cve_horario==3):
            materia3=materia.materia.nombre
            m3=color(materia)
            grupo3=materia.grupo
        elif(materia.horario.cve_horario==4):
            materia4=materia.materia.nombre
            m4=color(materia)
            grupo4=materia.grupo
        elif(materia.horario.cve_horario==5):
            materia5=materia.materia.nombre
            m5=color(materia)
            grupo5=materia.grupo
        elif(materia.horario.cve_horario==6):
            materia6=materia.materia.nombre
            m6=color(materia)
            grupo6=materia.grupo
        elif(materia.horario.cve_horario==7):
            materia7=materia.materia.nombre
            m7=color(materia)
            grupo7=materia.grupo
        elif(materia.horario.cve_horario==8):
            materia8=materia.materia.nombre
            m8=color(materia)
            grupo8=materia.grupo
        
        if(materia.horario.cve_horario==9):
            materia9=materia.materia.nombre
            m9=color(materia)
            grupo9=materia.grupo
        elif(materia.horario.cve_horario==10):
            materia10=materia.materia.nombre
            m10=color(materia)
            grupo10=materia.grupo
        elif(materia.horario.cve_horario==11):
            materia11=materia.materia.nombre
            m11=color(materia)
            grupo11=materia.grupo
        elif(materia.horario.cve_horario==12):
            materia12=materia.materia.nombre
            m12=color(materia)
            grupo12=materia.grupo
        elif(materia.horario.cve_horario==13):
            materia13=materia.materia.nombre
            m13=color(materia)
            grupo13=materia.grupo
        elif(materia.horario.cve_horario==14):
            materia14=materia.materia.nombre
            m14=color(materia)
            grupo14=materia.grupo
        elif(materia.horario.cve_horario==15):
            materia15=materia.materia.nombre
            m15=color(materia)
            grupo15=materia.grupo
        

    return render(request, 'profesor/main.html',locals(),context_instance=RequestContext(request))

def profesor_miperfil(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('profesor/mi-perfil.html',locals(),context_instance=RequestContext(request))

def profesor_preferencias(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('profesor/preferencias.html',locals(),context_instance=RequestContext(request))

def profesor_logout(request):
    return render_to_response('profesor/logout.html',locals(),context_instance=RequestContext(request))

def profesor_mis_grupos(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('profesor/mis-grupos.html',locals(),context_instance=RequestContext(request))

def profesor_registrar_calificaciones(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    grupolist = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    return render_to_response('profesor/registrar-calificaciones.html',locals(),context_instance=RequestContext(request))


def directorio(request):
    profesoresList= Profesor.objects.all()
    materiasList= Materia.objects.all()
    gruposList= Grupo.objects.all()
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('directorio.html',locals(),context_instance=RequestContext(request))

def profesor_reportes_PRUI08_1(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('profesor/reportes/PRUI08.1.html',locals(),context_instance=RequestContext(request))

def profesor_reportes_PRUI08_2(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('profesor/reportes/PRUI08.2.html',locals(),context_instance=RequestContext(request))

def profesor_calendario(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('profesor/calendario.html',locals(),context_instance=RequestContext(request))

def profesor_tutorias(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    usuario = request.user
    Tutorado=Alumno.objects.filter(tutor_escolar=usuario)
    print Tutorado
    return render_to_response('profesor/tutorias.html',locals(),context_instance=RequestContext(request))

def profesor_ingresa_calificacion(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materia=request.GET['materia']
    materiaGrupo = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)[int(materia)]
    request.session["materiaGrupo"] = materiaGrupo
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    print alumnos.values()
    return render_to_response('profesor/IngresaCalificacion.html',locals(),context_instance=RequestContext(request))

def profesor_guarda_calificacion(request):
    calificaciones=request.GET
    materiaGrupo = request.session["materiaGrupo"]
    print materiaGrupo
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    print "-"*10
    print alumnos.values()
    print "-"*10
    for alumno in calificaciones:
        p=alumnos.filter(alumno_id=alumno).update(calificacion=calificaciones.get(alumno))
        print p

    return render_to_response('profesor/registrar-calificaciones.html',locals(),context_instance=RequestContext(request))

def perfiles_profesor(request):
    cvep=request.GET['grup']
    profesor=Profesor.objects.get(cve_usuario__clave=cvep)
    nombre=profesor.cve_usuario.nombre + " " + profesor.cve_usuario.apellidoPaterno + " " + profesor.cve_usuario.apellidoMaterno
    rol=profesor.rol_academico
    clasificacion=profesor.cve_usuario.clasificacion
    email_i=profesor.cve_usuario.email_institucional
    email_p=profesor.cve_usuario.email_personal
    carrera=profesor.carrera
    telefono_c=profesor.cve_usuario.Telefono_Casa
    telefono=profesor.cve_usuario.Telefono_Celular
    grado=profesor.grado_estudios
    materias=MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    tutorados=Alumno.objects.filter(tutor_escolar=profesor)
    grupo=profesor.grupo_tutorado
    entrada=profesor.hora_entrada
    salida=profesor.hora_salida
    foto=profesor.cve_usuario.foto
    num=0
    for alumno in tutorados:
        num+=1
    num=8-num
    
    return render_to_response('perfiles/maldonadoCastilloIdalia.html',locals(),context_instance=RequestContext(request))

def perfiles_materia(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('perfiles/ingenieria-de-software.html',locals(),context_instance=RequestContext(request))


def perfiles_grupo(request):
    idg=request.GET['grup']
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materias=MateriaImpartidaEnGrupo.objects.filter(grupo__cve_grupo=idg)
    grupo=Grupo.objects.get(cve_grupo=idg)
    turno=grupo.turno
    print turno
    for materia in materias:
        if(turno=='Matutino'):
            print materia.horario.cve_horario
            if(materia.horario.cve_horario==1):
                materia1=materia.materia.nombre
                m1=color(materia)
                prof1=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==2):
                materia2=materia.materia.nombre
                m2=color(materia)
                prof2=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==3):
                materia3=materia.materia.nombre
                m3=color(materia)
                prof3=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==4):
                materia4=materia.materia.nombre
                m4=color(materia)
                prof4=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==5):
                materia5=materia.materia.nombre
                m5=color(materia)
                prof5=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==6):
                materia6=materia.materia.nombre
                m6=color(materia)
                prof6=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==7):
                materia7=materia.materia.nombre
                m7=color(materia)
                prof7=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==8):
                materia8=materia.materia.nombre
                m8=color(materia)
                prof8=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
        else:
            if(materia.horario.cve_horario==9):
                materia9=materia.materia.nombre
                m9=color(materia)
                prof9=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==10):
                materia10=materia.materia.nombre
                m10=color(materia)
                prof10=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==11):
                materia11=materia.materia.nombre
                m11=color(materia)
                prof11=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==12):
                materia12=materia.materia.nombre
                m12=color(materia)
                prof12=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==13):
                materia13=materia.materia.nombre
                m13=color(materia)
                prof13=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==14):
                materia14=materia.materia.nombre
                m14=color(materia)
                prof14=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            elif(materia.horario.cve_horario==15):
                materia15=materia.materia.nombre
                m15=color(materia)
                prof15=materia.profesor.cve_usuario.nombre+" "+materia.profesor.cve_usuario.apellidoPaterno+" "+materia.profesor.cve_usuario.apellidoMaterno
            
    return render_to_response('perfiles/3CM5.html',locals(),context_instance=RequestContext(request))   

def profesor_tutorias_comentar(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    cont =0
    usuario = request.user
    Tutorado=Alumno.objects.filter(tutor_escolar=usuario)
    return render_to_response('profesor/comentar-tutoria.html',locals(),context_instance=RequestContext(request))

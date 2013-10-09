# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response,get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from forms import *
from models import *
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json


from geraldo import Report, ReportBand, DetailBand, SystemField, Label, ObjectValue
from geraldo.utils import cm
from geraldo.generators import PDFGenerator

from django.http import HttpResponse    
from reports import lista_alumnos,lista_evaluaciones
from geraldo.generators import PDFGenerator



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

@login_required(login_url='/inicio')
def profesor_main(request):
    try:
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
    except:
        mensaje=1
        return render(request, 'profesor/main.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/inicio')    
def profesor_miperfil(request):
    try:
        profesor=request.user
        atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
        profesor2=Profesor.objects.get(cve_usuario=profesor)
        materias=MateriaImpartidaEnGrupo.objects.filter(profesor=profesor2)
        tutorados=Alumno.objects.filter(tutor_escolar=profesor2)
        foto=profesor2.cve_usuario.foto
        num=0
        for alumno in tutorados:
            num+=1
        num=8-num
        return render_to_response('profesor/mi-perfil.html',locals(),context_instance=RequestContext(request))
    except:
        mensaje=1
        return render_to_response('profesor/mi-perfil.html',locals(),context_instance=RequestContext(request))

def guarda_miperfil(request):
    try:
        profesor=request.user
        atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
        grupos=MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
        profesor2=Profesor.objects.get(cve_usuario=profesor)
        correo=request.GET['email']
        telefono=request.GET['telefono']
        hentrada=request.GET['entrada']
        hsalida=request.GET['salida']
        try:
            foto="fotos/"+request.GET['imagen']
        except:
            foto=profesor2.cve_usuario.foto
        usuario=Usuario.objects.filter(clave=profesor).update(email_personal=correo,Telefono_Casa=telefono, foto=foto)
        p=Profesor.objects.filter(cve_usuario=profesor).update(hora_entrada=hentrada,hora_salida=hsalida)

        profesor2=Profesor.objects.get(cve_usuario=profesor)
        materias=MateriaImpartidaEnGrupo.objects.filter(profesor=profesor2)
        tutorados=Alumno.objects.filter(tutor_escolar=profesor2)
        foto=profesor2.cve_usuario.foto
        num=0
        for alumno in tutorados:
            num+=1
        num=8-num
        mensaje=1
        return render_to_response('profesor/mi-perfil2.html',locals(),context_instance=RequestContext(request))
    except:
        mensaje=2
        profesor=request.user
        atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
        profesor2=Profesor.objects.get(cve_usuario=profesor)
        materias=MateriaImpartidaEnGrupo.objects.filter(profesor=profesor2)
        tutorados=Alumno.objects.filter(tutor_escolar=profesor2)
        foto=profesor2.cve_usuario.foto
        num=0
        for alumno in tutorados:
            num+=1
        num=8-num
        return render_to_response('profesor/mi-perfil2.html',locals(),context_instance=RequestContext(request))


def profesor_miperfil2(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    profesor2=Profesor.objects.get(cve_usuario=profesor)
    grupos=MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    return render_to_response('profesor/mi-perfil2.html',locals(),context_instance=RequestContext(request))


def profesor_preferencias(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    prof=Profesor.objects.get(cve_usuario=profesor)
    return render_to_response('profesor/preferencias.html',locals(),context_instance=RequestContext(request))


def guardar_preferencias(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    comentario=request.GET['preferencias']
    p=Profesor.objects.filter(cve_usuario=profesor).update(comentario=comentario)
    prof=Profesor.objects.get(cve_usuario=profesor)
    mensaje=1
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

def profesor_registrar_calificaciones_extra(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    grupolist = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    return render_to_response('profesor/registrar-calificacionesExtra.html',locals(),context_instance=RequestContext(request))

def profesor_registrar_calificaciones_ets(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    grupolist = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    return render_to_response('profesor/registrar-calificacionesETS.html',locals(),context_instance=RequestContext(request))




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
    grupolist = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    return render_to_response('profesor/reportes/PRUI08.1.html',locals(),context_instance=RequestContext(request))

def profesor_reportes_PRUI08_2(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    grupolist = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
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
    request.session["materia"] = materia
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    #print alumnos.values()
    return render_to_response('profesor/IngresaCalificacion.html',locals(),context_instance=RequestContext(request))

def profesor_ingresa_calificacion_extra(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materia=request.GET['materia']
    materiaGrupo = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)[int(materia)]
    request.session["materiaGrupo"] = materiaGrupo
    request.session["materia"] = materia
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    print alumnos.values()
    return render_to_response('profesor/IngresaCalificacionExtra.html',locals(),context_instance=RequestContext(request))

def profesor_ingresa_calificacion_ets(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materia=request.GET['materia']
    materiaGrupo = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)[int(materia)]
    request.session["materiaGrupo"] = materiaGrupo

    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    print alumnos.values()
    return render_to_response('profesor/IngresaCalificacionETS.html',locals(),context_instance=RequestContext(request))

def profesor_guarda_calificacion(request):
    calificaciones=request.GET
    profesor=request.user
    grupolist = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materiaGrupo = request.session["materiaGrupo"]
    materia = request.session["materia"]
    print materiaGrupo
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    print "-"*10
    print alumnos.values()
    print "-"*10
    for alumno in calificaciones:
        p=alumnos.filter(alumno_id=alumno).update(calificacion=calificaciones.get(alumno))
        print p
    mensaje=1
    return render_to_response('profesor/IngresaCalificacion.html',locals(),context_instance=RequestContext(request))



def profesor_guarda_calificacionExtra(request):
    calificaciones=request.GET
    profesor=request.user
    grupolist = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materiaGrupo = request.session["materiaGrupo"]
    print materiaGrupo
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    print "-"*10
    print alumnos.values()
    print "-"*10
    for alumno in calificaciones:
        p=alumnos.filter(alumno_id=alumno).update(calificacionExtra=calificaciones.get(alumno))
        print p

    return render_to_response('profesor/registrar-calificacionesExtra.html',locals(),context_instance=RequestContext(request))

def profesor_guarda_calificacionETS(request):
    calificaciones=request.GET
    profesor=request.user
    grupolist = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materiaGrupo = request.session["materiaGrupo"]
    print materiaGrupo
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    print "-"*10
    print alumnos.values()
    print "-"*10
    for alumno in calificaciones:
        p=alumnos.filter(alumno_id=alumno).update(calificacion=calificaciones.get(alumno))
        print p

    return render_to_response('profesor/registrar-calificacionesETS.html',locals(),context_instance=RequestContext(request))

def perfiles_profesor(request):
        try:
            profesor=request.user
            atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
            cvep=request.GET['prof']
            profesor2=Profesor.objects.get(cve_usuario__clave=cvep)
            nombre=profesor2.cve_usuario.nombre + " " + profesor2.cve_usuario.apellidoPaterno + " " + profesor2.cve_usuario.apellidoMaterno
            rol=profesor2.rol_academico
            clasificacion=profesor2.cve_usuario.clasificacion
            email_i=profesor2.cve_usuario.email_institucional
            email_p=profesor2.cve_usuario.email_personal
            carrera=profesor2.carrera
            telefono_c=profesor2.cve_usuario.Telefono_Casa
            telefono=profesor2.cve_usuario.Telefono_Celular
            grado=profesor2.grado_estudios
            materias=MateriaImpartidaEnGrupo.objects.filter(profesor=profesor2)
            tutorados=Alumno.objects.filter(tutor_escolar=profesor2)
            grupo=profesor2.grupo_tutorado
            entrada=profesor2.hora_entrada
            salida=profesor2.hora_salida
            foto=profesor2.cve_usuario.foto
            num=0
            for alumno in tutorados:
                num+=1
            num=8-num
            return render_to_response('perfiles/maldonadoCastilloIdalia.html',locals(),context_instance=RequestContext(request))
        except:
            profesoresList= Profesor.objects.all()
            materiasList= Materia.objects.all()
            gruposList= Grupo.objects.all()
            profesor=request.user
            atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
            mensaje=1
            return render_to_response('directorio.html',locals(),context_instance=RequestContext(request))
            

def perfiles_materia(request):
    try:
        profesor=request.user
        atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
        infmat=request.GET['mat']

        materia2=Materia.objects.get(nombre=infmat)
        nombre=materia2.nombre
        creditos=materia2.creditos
        clasificacion=materia2.clasificacion
        nivel=materia2.nivel
        coordinador=materia2.coordinador
        departamento=materia2.depto.nombre_depto
        materias=MateriaImpartidaEnGrupo.objects.filter(materia=materia2)
        
        return render_to_response('perfiles/ingenieria-de-software.html',locals(),context_instance=RequestContext(request))

    except:
        profesoresList= Profesor.objects.all()
        materiasList= Materia.objects.all()
        gruposList= Grupo.objects.all()
        profesor=request.user
        atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
        mensaje=1
        return render_to_response('directorio.html',locals(),context_instance=RequestContext(request))

def perfiles_grupo(request):
    try:
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
    except:
            profesoresList= Profesor.objects.all()
            materiasList= Materia.objects.all()
            gruposList= Grupo.objects.all()
            profesor=request.user
            atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
            mensaje=1
            return render_to_response('directorio.html',locals(),context_instance=RequestContext(request))

def profesor_tutorias_comentar(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    cont =0
    usuario = request.user
    Tutorado=ComentarioTutorado.objects.filter(profesor=usuario)
    return render_to_response('profesor/comentar-tutoria.html',locals(),context_instance=RequestContext(request))

def guardar_comentarios(request):
    try:
        profesor=request.user
        atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
        cont =0
        usuario = request.user
        Tutorado=ComentarioTutorado.objects.filter(profesor=usuario)
        comentarios=request.GET
        for alumno in comentarios:
            p=Tutorado.filter(alumno_id=alumno).update(comentario=comentarios.get(alumno))
        mensaje=1
        return render_to_response('profesor/comentar-tutoria.html',locals(),context_instance=RequestContext(request))
    except:
        profesor=request.user
        atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
        cont =0
        usuario = request.user
        Tutorado=ComentarioTutorado.objects.filter(profesor=usuario)
        mensaje=2
        return render_to_response('profesor/comentar-tutoria.html',locals(),context_instance=RequestContext(request))

def profesor_agregar_tutorado(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    return render_to_response('profesor/agregar-tutorado.html',locals(),context_instance=RequestContext(request))

def profesor_tutorias_add(request):
    try:
        profesor=request.user
        aprofesor = Profesor.objects.get(cve_usuario = profesor)
        boleta = request.GET['boleta']
        alumno=Alumno.objects.get(cve_usuario__clave=boleta)
        if alumno.tipo == 'Historico':
            mensaje = 5
            return render_to_response('profesor/agregar-tutorado.html',locals(),context_instance=RequestContext(request))
        elif alumno.tutor_escolar == None:
            alumno.tutor_escolar=aprofesor
            alumno.save()
        else:
            mensaje=4
            return render_to_response('profesor/agregar-tutorado.html',locals(),context_instance=RequestContext(request))
        p = ComentarioTutorado(profesor=aprofesor, alumno=alumno, comentario="")
        p.save()
        mensaje=1
        return render_to_response('profesor/agregar-tutorado.html',locals(),context_instance=RequestContext(request))
    except:
        mensaje=2
        profesor=request.user
        atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
        return render_to_response('profesor/agregar-tutorado.html',locals(),context_instance=RequestContext(request))


def reporte_lista(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materia=request.GET['materia']
    materiaGrupo = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)[int(materia)]
    request.session["materiaGrupo"] = materiaGrupo
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)
    resp = HttpResponse(mimetype='application/pdf')
    report = lista_alumnos(queryset=alumnos)
    report.generate_by(PDFGenerator, filename=resp)
    return resp


def reporte_evaluaciones(request):
    profesor=request.user
    atributos_profesor = Profesor.objects.filter(cve_usuario = profesor)[0]
    materia=request.GET['materia']
    materiaGrupo = MateriaImpartidaEnGrupo.objects.filter(profesor=profesor)[int(materia)]
    request.session["materiaGrupo"] = materiaGrupo
    alumnos = AlumnoTomaClaseEnGrupo.objects.filter(materia_grupo=materiaGrupo)

    resp = HttpResponse(mimetype='application/pdf')
    report = lista_evaluaciones(queryset=alumnos)
    report.generate_by(PDFGenerator, filename=resp)
    return resp


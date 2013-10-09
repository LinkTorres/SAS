# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, _user_has_perm, PermissionsMixin, _user_has_module_perms
from datetime import datetime, time, date
from managers import UsuarioManager
from django.db.models.signals import *
from django.dispatch import receiver
from django.core.validators import RegexValidator

generos=(('M', 'Masculino'),('F', 'Femenino'))
clasificaciones=(('Alumnos', 'Alumnos'),('Profesores', 'Profesores'),('Empleado_escolar','Empleado_escolar'))
clasificacion_materias=(('Institucional', 'Institucional'),('Cientifica_basica', 'Científica_basica'),
                ('Profesional', 'Profesional'),('Terminal_integracion', 'Terminal_integración'))
tipo_materias=(('Obligatoria', 'Obligatoria'),('Optativa', 'Optativa'))
niveles=(('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'))
turnos=(('M', 'Matituno'),('V', 'Vespertino'))
tipos_laboratorios=(('Electronica', 'Electrónica'),('Sistemas', 'Sistemas'),
        ('Programacion', 'Programación'),('Basicas', 'Básicas'),('Redes', 'Redes'))
dias=(('lunes', 'lunes'),('martes', 'martes'),('miercoles', 'miércoles'),('jueves', 'jueves'),('viernes', 'viernes'))
seguros_Medico=(('IMSS','IMSS'),('ISSTE','ISSTE'))
tipos_alumnos=(('Historico','Histórico'),('Nuevo_Ingreso','Nuevo Ingreso'),('Regular','Regular'),('Irregular','Irregular'))
status_empleados=(('Activo', 'Activo'),('Sabatico', 'Sabático'),('Incapacidad','Incapacidad'))
roles_academicos=(('Coordinador', 'Coordinador'),('JefeAsignatura', 'JefeAsignatura'),('Normal','Normal'))
tipo_profesores=(('Base', 'Base'),('Interino', 'Interino'))
turno =(('Matutino','Matutino'),('Vespertino','Vespertino'))


#***********************************************************************************************************
class Usuario(AbstractBaseUser, PermissionsMixin):

    clave = models.CharField(max_length=10, unique=True, db_index=True)
    nombre = models.CharField(max_length=30)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    email_personal = models.EmailField(max_length=70,null=True,blank=True)
    email_institucional = models.EmailField(max_length=70)
    Telefono_Casa = models.IntegerField(blank=True,null=True)
    Telefono_Celular = models.IntegerField(blank=True,null=True)
    seguroMedico= models.CharField(max_length=10, choices=seguros_Medico,null=True,blank=True)
    numero_ss = models.CharField(max_length=20)
    seguro_social_institucion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=30)
    municipio_o_delegacion = models.CharField(max_length=30)
    calle = models.CharField(max_length=20, blank=True,null=True)
    colonia = models.CharField(max_length=20, blank=True,null=True)
    lt = models.IntegerField(blank=True,null=True)
    num = models.IntegerField(blank=True,null=True)
    mz = models.IntegerField(blank=True,null=True)
    cp = models.IntegerField(blank=True,null=True)
    alergias = models.CharField(max_length=80,blank=True,null=True)
    enfermedades= models.CharField(max_length=80,blank=True,null=True)
    nacionalidad = models.CharField(max_length=15)
    sexo = models.CharField(max_length=10, choices=generos)
    tipo_sangre = models.CharField(max_length=20, blank=True,null=True)
    foto=models.ImageField(upload_to='fotos',verbose_name='Foto', blank=True,null=True)
    fecha_alta = models.DateField(default=date.today,blank=True,null=True)
    fecha_nac = models.DateField( blank=True,null=True)

    activo = models.BooleanField(default=True, help_text='Activa un usuario para poder usar el sistema')
    administrador = models.BooleanField(default=False, help_text='Que usuarios se les permite entrar al administrador')
    clasificacion = models.CharField(max_length=30, choices=clasificaciones)
    objects = UsuarioManager()
    USERNAME_FIELD = 'clave'

    def get_full_name(self):
        return self.apellidoPaterno + ' ' + self.apellidoMaterno + ' ' +self.nombre

    def get_full_name_prof(self):
        return 'Profesor : '+self.apellidoPaterno + ' ' + self.apellidoMaterno + ' ' +self.nombre

    def get_short_name(self):
        return self.nombre

    def __unicode__(self):
        return self.clave

    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.administrador

    @property
    def is_active(self):
        return self.activo

#***********************************************************************************************************

class Salon(models.Model):
    cve_salon = models.IntegerField(unique=True, db_index=True) #primary_key=True
   
    def __unicode__(self):
        return str(self.cve_salon)

#***********************************************************************************************************

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=30, unique=True, db_index=True)
    tipo = models.CharField(max_length=20, choices=tipos_laboratorios)
    ubicacion = models.CharField(max_length=30, blank=True,null=True)
    
    def __unicode__(self):
        return self.nombre

#***********************************************************************************************************
class EmpleadoEscolar(models.Model):
    cve_usuario = models.ForeignKey(Usuario,unique=True, db_index=True)
    status = models.CharField(max_length=20, choices=status_empleados)
    hora_entrada = models.CharField(max_length=5)
    hora_salida = models.CharField(max_length=5)
    grado_estudios = models.CharField(max_length=30 )
    carrera = models.CharField(max_length=40)
    salario = models.FloatField(null=True,blank=True)
    lab_a_mi_cargo = models.ForeignKey(Laboratorio, null=True,blank=True)
    def __unicode__(self):
        return str(self.cve_usuario)

#***********************************************************************************************************

class Grupo(models.Model):
    cve_grupo = models.CharField(max_length=4, unique=True, db_index=True)
    cve_salon = models.ForeignKey(Salon)
    turno = models.CharField(max_length=30, choices=turno)
    def __unicode__(self):
        return self.cve_grupo

class Depto(models.Model):
    nombre_depto = models.CharField(max_length=30,unique=True, db_index=True)
    ubicacion = models.CharField(max_length=50, blank=True,null=True)
    jefe_depto = models.ForeignKey(Usuario,blank=True,null=True)
    def __unicode__(self):
        return self.nombre_depto

class Horario(models.Model):
    cve_horario = models.IntegerField(unique=True,db_index=True)
    class Meta:
        ordering = ('cve_horario',)
    def __unicode__(self):
        return str(self.cve_horario)


#***********************************************************************************************************
class Materia(models.Model):
    cve_materia = models.CharField(max_length=4, unique=True, db_index=True)
    nombre = models.CharField(max_length=30)
    creditos = models.FloatField()
    plan_estudios = models.CharField(max_length=4)
    clasificacion = models.CharField(max_length=30, choices=clasificacion_materias)
    tipo= models.CharField(max_length=12, choices=tipo_materias)
    nivel = models.CharField(max_length=1, choices=niveles)
    coordinador = models.ForeignKey(Usuario,blank=True,null=True)
    depto = models.ForeignKey(Depto,blank=True,null=True)
    materia_antecedente = models.ForeignKey('self', null=True,blank=True,related_name='materia_materia_antecedente')
    materia_siguiente = models.ForeignKey('self', null=True, blank=True, related_name='materia_materia_siguiente')
    def __unicode__(self):
        return '%s %s' % (self.cve_materia,self.nombre)


class Profesor(models.Model):
    
    cve_usuario = models.ForeignKey(Usuario)
    rol_academico = models.CharField(max_length=30, choices=roles_academicos,null=True)
    tipo = models.CharField(max_length=30, choices=tipo_profesores)
    grupo_tutorado = models.ForeignKey(Grupo,null=True,blank=True)

    status = models.CharField(max_length=20, choices=status_empleados)
    hora_entrada = models.CharField(max_length=5)
    hora_salida = models.CharField(max_length=5)
    grado_estudios = models.CharField(max_length=30 )
    carrera = models.CharField(max_length=40)
    salario = models.FloatField(null=True,blank=True)
    lab_a_mi_cargo = models.ForeignKey(Laboratorio, null=True,blank=True)
    comentario=models.CharField(max_length=400)

    def __unicode__(self):
        return str(self.cve_usuario)


class MateriaImpartidaEnGrupo(models.Model):
    materia = models.ForeignKey(Materia)
    grupo = models.ForeignKey(Grupo)
    horario = models.ForeignKey(Horario)
    profesor = models.ForeignKey(Profesor)

    class Meta:
        unique_together = (("materia", "grupo"),("grupo", "horario"))
    def __str__(self):
        return '%s %s' % (self.materia, self.grupo)






#***********************************************************************************************************

class Alumno(models.Model):
    cve_usuario= models.ForeignKey(Usuario,unique=True, db_index=True)
    escuela_procedencia = models.CharField(max_length=50)
    tipo= models.CharField(max_length=20, choices=tipos_alumnos)
    promedio_escuela_procedencia = models.FloatField()
    tutor_legal = models.CharField(max_length=50)
    tutor_escolar = models.ForeignKey(Profesor,null=True,blank=True)
    def __unicode__(self):
        return str(self.cve_usuario)
#***********************************************************************************************************


#***********************************************************************************************************




#***********************************************************************************************************
class Ets(models.Model):
    cve_materia = models.ForeignKey(Materia)
    turno = models.CharField(max_length=1,choices=turnos)
    fecha = models.DateField()
    hora = models.TimeField()
    evaluador = models.ForeignKey(Profesor)
    salon=models.ForeignKey(Salon)

    class Meta:
        unique_together = (("cve_materia", "turno"),)
        ordering = ('cve_materia',)

    def __unicode__(self): 
        return '%s %s' % (str(self.cve_materia), self.turno)

#***********************************************************************************************************



#***********************************************************************************************************



#***********************************************************************************************************

class MateriaImpartidaEnLab(models.Model):
    cve_materia_grupo = models.ForeignKey(MateriaImpartidaEnGrupo)
    nombre_lab = models.ForeignKey(Laboratorio)
    dia = models.CharField(max_length=10,choices=dias)

    class Meta:
        unique_together = (("cve_materia_grupo", "nombre_lab"),)
        ordering = ('nombre_lab',)

    def __str__(self):
        return '%s %s' % (self.cve_materia_grupo, self.nombre_lab)

#***********************************************************************************************************

class AlumnoTomaEts(models.Model):
    alumno = models.ForeignKey(Alumno)
    ets = models.ForeignKey(Ets)
    calificacion = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = (("alumno", "ets"),)
        ordering = ('alumno',)

    def __str__(self):
        return '%s %s' % (self.alumno,self.ets)




#***********************************************************************************************************
class ComentarioTutorado(models.Model):
    profesor = models.ForeignKey(Profesor)
    alumno = models.ForeignKey(Alumno)
    comentario=models.CharField(max_length=150)
    fecha=models.DateField(default=date.today,blank=True,null=True)
    class Meta:
        unique_together = (("profesor","alumno"),)
        ordering = ('alumno',)
    def __str__(self):
        return '%s %s' % (self.alumno,self.comentario)
#***********************************************************************************************************
class AlumnoTomaClaseEnGrupo(models.Model):
    alumno = models.ForeignKey(Alumno)
    materia_grupo = models.ForeignKey(MateriaImpartidaEnGrupo)
    calificacion=models.IntegerField(null=True, blank=True)
    calificacionExtra=models.IntegerField(null=True, blank=True)
    class Meta:
        unique_together = (("alumno", "materia_grupo"),)
        ordering = ('alumno',)
    def __str__(self):
        return '%s %s' % (self.alumno,self.materia_grupo)

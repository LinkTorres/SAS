#encoding:utf-8
from models import *
from forms import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, Permission

admin.site.unregister(Site)
admin.site.unregister(Group)

class MyUserAdmin(UserAdmin):
    form = CambiarusuarioForm
    add_form = CrearusuarioForm

    list_display = ('clave', 'nombre')
    list_filter = ('administrador','activo')
    
    fieldsets = (
                ('Autentificación', {'fields': ('nombre','apellidoPaterno','apellidoMaterno','clave',
                'password','clasificacion','curp','nacionalidad','sexo','email_personal','email_institucional','Telefono_Casa','Telefono_Celular','numero_ss',
               'seguroMedico', 'seguro_social_institucion')}),
                ('Personal', {'fields': ('estado', 'municipio_o_delegacion', 'calle', 'colonia',
                    'lt','num','mz','cp','alergias','enfermedades','tipo_sangre','foto','fecha_alta','fecha_nac')}),
                ('Permisos', {'fields': ('administrador', 'activo', 'is_superuser', 'user_permissions')}),
    )
    add_fieldsets = (
                    (None, {'classes': ('wide',), 'fields': ('clave', 'password1', 'password2',)}),
    )
    search_fields = ('clave','nombre')
    ordering = ('clave',)
    filter_horizontal = ('user_permissions',)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'user_permissions':
            query = Permission.objects.filter(content_type__app_label="principal")
            kwargs['queryset'] = query
        return super(MyUserAdmin, self).formfield_for_manytomany(db_field, request=request, **kwargs)


    
admin.site.register(Usuario, MyUserAdmin)
admin.site.register(Salon)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(EmpleadoEscolar)
admin.site.register(Grupo)
admin.site.register(Materia)
admin.site.register(Depto)
admin.site.register(Ets)
admin.site.register(Laboratorio)
admin.site.register(MateriaImpartidaEnLab)
admin.site.register(AlumnoTomaEts)
admin.site.register(Horario)
admin.site.register(MateriaImpartidaEnGrupo)
admin.site.register(ComentarioTutorado)

admin.site.register(AlumnoTomaClaseEnGrupo)
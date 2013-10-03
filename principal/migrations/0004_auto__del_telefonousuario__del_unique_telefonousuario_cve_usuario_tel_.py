# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'TelefonoUsuario', fields ['cve_usuario', 'tel']
        db.delete_unique(u'principal_telefonousuario', ['cve_usuario_id', 'tel'])

        # Deleting model 'TelefonoUsuario'
        db.delete_table(u'principal_telefonousuario')

        # Adding field 'Usuario.Telefono_Casa'
        db.add_column(u'principal_usuario', 'Telefono_Casa',
                      self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Usuario.Telefono_Celular'
        db.add_column(u'principal_usuario', 'Telefono_Celular',
                      self.gf('django.db.models.fields.IntegerField')(max_length=15, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'TelefonoUsuario'
        db.create_table(u'principal_telefonousuario', (
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=30)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], unique=True)),
        ))
        db.send_create_signal(u'principal', ['TelefonoUsuario'])

        # Adding unique constraint on 'TelefonoUsuario', fields ['cve_usuario', 'tel']
        db.create_unique(u'principal_telefonousuario', ['cve_usuario_id', 'tel'])

        # Deleting field 'Usuario.Telefono_Casa'
        db.delete_column(u'principal_usuario', 'Telefono_Casa')

        # Deleting field 'Usuario.Telefono_Celular'
        db.delete_column(u'principal_usuario', 'Telefono_Celular')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'principal.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'cve_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Usuario']", 'unique': 'True'}),
            'escuela_procedencia': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promedio_escuela_procedencia': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tutor_escolar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'null': 'True', 'blank': 'True'}),
            'tutor_legal': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'principal.alumnotomaclaseengrupo': {
            'Meta': {'ordering': "('alumno',)", 'unique_together': "(('alumno', 'materia_grupo'),)", 'object_name': 'AlumnoTomaClaseEnGrupo'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Alumno']"}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.MateriaImpartidaEnGrupo']"})
        },
        u'principal.alumnotomaets': {
            'Meta': {'ordering': "('alumno',)", 'unique_together': "(('alumno', 'ets'),)", 'object_name': 'AlumnoTomaEts'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Alumno']"}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ets': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Ets']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.depto': {
            'Meta': {'object_name': 'Depto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jefe_depto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'null': 'True', 'blank': 'True'}),
            'nombre_depto': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'principal.empleadoescolar': {
            'Meta': {'object_name': 'EmpleadoEscolar'},
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'cve_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Usuario']", 'unique': 'True'}),
            'grado_estudios': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'hora_entrada': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'hora_salida': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_a_mi_cargo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Laboratorio']", 'null': 'True', 'blank': 'True'}),
            'salario': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'principal.ets': {
            'Meta': {'ordering': "('cve_materia',)", 'unique_together': "(('cve_materia', 'turno'),)", 'object_name': 'Ets'},
            'cve_materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']"}),
            'evaluador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'hora': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'salon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Salon']"}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'principal.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'cve_grupo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4', 'db_index': 'True'}),
            'cve_salon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Salon']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.horario': {
            'Meta': {'ordering': "('cve_horario',)", 'object_name': 'Horario'},
            'cve_horario': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jueves': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'lunes': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'martes': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'miercoles': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'viernes': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'})
        },
        u'principal.laboratorio': {
            'Meta': {'object_name': 'Laboratorio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'principal.materia': {
            'Meta': {'object_name': 'Materia'},
            'clasificacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'coordinador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'null': 'True', 'blank': 'True'}),
            'creditos': ('django.db.models.fields.FloatField', [], {}),
            'cve_materia': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4', 'db_index': 'True'}),
            'depto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Depto']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_antecedente': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'materia_materia_antecedente'", 'null': 'True', 'to': u"orm['principal.Materia']"}),
            'materia_siguiente': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'materia_materia_siguiente'", 'null': 'True', 'to': u"orm['principal.Materia']"}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'plan_estudios': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'principal.materiaimpartidaengrupo': {
            'Meta': {'unique_together': "(('materia', 'grupo'), ('grupo', 'horario'))", 'object_name': 'MateriaImpartidaEnGrupo'},
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Grupo']"}),
            'horario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Horario']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']"})
        },
        u'principal.materiaimpartidaenlab': {
            'Meta': {'ordering': "('nombre_lab',)", 'unique_together': "(('cve_materia_grupo', 'nombre_lab'),)", 'object_name': 'MateriaImpartidaEnLab'},
            'cve_materia_grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.MateriaImpartidaEnGrupo']"}),
            'dia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_lab': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Laboratorio']"})
        },
        u'principal.profesor': {
            'Meta': {'object_name': 'Profesor'},
            'cve_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.EmpleadoEscolar']"}),
            'grupo_tutorado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Grupo']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rol_academico': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'principal.profesordaclaseengrupo': {
            'Meta': {'ordering': "('profesor',)", 'unique_together': "(('profesor', 'materia_grupo'),)", 'object_name': 'ProfesorDaClaseEnGrupo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.MateriaImpartidaEnGrupo']"}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']"})
        },
        u'principal.profesorimpartemateria': {
            'Meta': {'ordering': "('profesor',)", 'unique_together': "(('profesor', 'materia'),)", 'object_name': 'ProfesorImparteMateria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']"}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']"})
        },
        u'principal.salon': {
            'Meta': {'object_name': 'Salon'},
            'cve_salon': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'Telefono_Casa': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'Telefono_Celular': ('django.db.models.fields.IntegerField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'administrador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alergias': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'apellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'clasificacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'clave': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'db_index': 'True'}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'curp': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'email_institucional': ('django.db.models.fields.EmailField', [], {'max_length': '70'}),
            'email_personal': ('django.db.models.fields.EmailField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'enfermedades': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fecha_alta': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            'fecha_nac': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'municipio_o_delegacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nacionalidad': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numero_ss': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'seguroMedico': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'seguro_social_institucion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tipo_sangre': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['principal']
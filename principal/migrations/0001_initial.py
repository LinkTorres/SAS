# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'principal_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clave', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10, db_index=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellidoPaterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellidoMaterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('curp', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('email_personal', self.gf('django.db.models.fields.EmailField')(max_length=70, null=True, blank=True)),
            ('email_institucional', self.gf('django.db.models.fields.EmailField')(max_length=70)),
            ('numero_ss', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('seguro_social_institucion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('municipio_o_delegacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('lt', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mz', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cp', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('alergias', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('enfermedades', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('nacionalidad', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('tipo_sangre', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('fecha_alta', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_nac', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('administrador', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clasificacion', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'principal', ['Usuario'])

        # Adding M2M table for field groups on 'Usuario'
        m2m_table_name = db.shorten_name(u'principal_usuario_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm[u'principal.usuario'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'Usuario'
        m2m_table_name = db.shorten_name(u'principal_usuario_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm[u'principal.usuario'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'permission_id'])

        # Adding model 'Salon'
        db.create_table(u'principal_salon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_salon', self.gf('django.db.models.fields.IntegerField')(unique=True, db_index=True)),
        ))
        db.send_create_signal(u'principal', ['Salon'])

        # Adding model 'Laboratorio'
        db.create_table(u'principal_laboratorio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, db_index=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Laboratorio'])

        # Adding model 'EmpleadoEscolar'
        db.create_table(u'principal_empleadoescolar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], unique=True)),
            ('hora_entrada', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('hora_salida', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('grado_estudios', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('salario', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lab_a_mi_cargo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Laboratorio'], null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['EmpleadoEscolar'])

        # Adding model 'Grupo'
        db.create_table(u'principal_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_grupo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4, db_index=True)),
            ('cve_salon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Salon'])),
        ))
        db.send_create_signal(u'principal', ['Grupo'])

        # Adding model 'Profesor'
        db.create_table(u'principal_profesor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.EmpleadoEscolar'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('grupo_tutorado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Grupo'], null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Profesor'])

        # Adding model 'Alumno'
        db.create_table(u'principal_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], unique=True)),
            ('escuela_procedencia', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('promedio_escuela_procedencia', self.gf('django.db.models.fields.FloatField')()),
            ('tutor_legal', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tutor_escolar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Alumno'])

        # Adding model 'TelefonoUsuario'
        db.create_table(u'principal_telefonousuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], unique=True)),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'principal', ['TelefonoUsuario'])

        # Adding unique constraint on 'TelefonoUsuario', fields ['cve_usuario', 'tel']
        db.create_unique(u'principal_telefonousuario', ['cve_usuario_id', 'tel'])

        # Adding model 'Depto'
        db.create_table(u'principal_depto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_depto', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, db_index=True)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('jefe_depto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Depto'])

        # Adding model 'Materia'
        db.create_table(u'principal_materia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_materia', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4, db_index=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('creditos', self.gf('django.db.models.fields.FloatField')()),
            ('plan_estudios', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('coordinador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], null=True, blank=True)),
            ('depto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Depto'], null=True, blank=True)),
            ('materia_antecedente', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='materia_materia_antecedente', null=True, to=orm['principal.Materia'])),
            ('materia_siguiente', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='materia_materia_siguiente', null=True, to=orm['principal.Materia'])),
        ))
        db.send_create_signal(u'principal', ['Materia'])

        # Adding model 'Ets'
        db.create_table(u'principal_ets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Materia'])),
            ('turno', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('hora', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('evaluador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'])),
            ('salon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Salon'])),
        ))
        db.send_create_signal(u'principal', ['Ets'])

        # Adding unique constraint on 'Ets', fields ['cve_materia', 'turno']
        db.create_unique(u'principal_ets', ['cve_materia_id', 'turno'])

        # Adding model 'Horario'
        db.create_table(u'principal_horario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_horario', self.gf('django.db.models.fields.IntegerField')(unique=True, db_index=True)),
            ('lunes', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('martes', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('miercoles', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('jueves', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('viernes', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Horario'])

        # Adding model 'MateriaImpartidaEnGrupo'
        db.create_table(u'principal_materiaimpartidaengrupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Materia'])),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Grupo'])),
            ('horario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Horario'])),
        ))
        db.send_create_signal(u'principal', ['MateriaImpartidaEnGrupo'])

        # Adding unique constraint on 'MateriaImpartidaEnGrupo', fields ['materia', 'grupo']
        db.create_unique(u'principal_materiaimpartidaengrupo', ['materia_id', 'grupo_id'])

        # Adding unique constraint on 'MateriaImpartidaEnGrupo', fields ['grupo', 'horario']
        db.create_unique(u'principal_materiaimpartidaengrupo', ['grupo_id', 'horario_id'])

        # Adding model 'MateriaImpartidaEnLab'
        db.create_table(u'principal_materiaimpartidaenlab', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_materia_grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.MateriaImpartidaEnGrupo'])),
            ('nombre_lab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Laboratorio'])),
            ('dia', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'principal', ['MateriaImpartidaEnLab'])

        # Adding unique constraint on 'MateriaImpartidaEnLab', fields ['cve_materia_grupo', 'nombre_lab']
        db.create_unique(u'principal_materiaimpartidaenlab', ['cve_materia_grupo_id', 'nombre_lab_id'])

        # Adding model 'AlumnoTomaEts'
        db.create_table(u'principal_alumnotomaets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
            ('ets', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Ets'])),
            ('calificacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['AlumnoTomaEts'])

        # Adding unique constraint on 'AlumnoTomaEts', fields ['alumno', 'ets']
        db.create_unique(u'principal_alumnotomaets', ['alumno_id', 'ets_id'])

        # Adding model 'ProfesorImparteMateria'
        db.create_table(u'principal_profesorimpartemateria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'])),
            ('materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Materia'])),
        ))
        db.send_create_signal(u'principal', ['ProfesorImparteMateria'])

        # Adding unique constraint on 'ProfesorImparteMateria', fields ['profesor', 'materia']
        db.create_unique(u'principal_profesorimpartemateria', ['profesor_id', 'materia_id'])

        # Adding model 'ProfesorDaClaseEnGrupo'
        db.create_table(u'principal_profesordaclaseengrupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'])),
            ('materia_grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.MateriaImpartidaEnGrupo'])),
        ))
        db.send_create_signal(u'principal', ['ProfesorDaClaseEnGrupo'])

        # Adding unique constraint on 'ProfesorDaClaseEnGrupo', fields ['profesor', 'materia_grupo']
        db.create_unique(u'principal_profesordaclaseengrupo', ['profesor_id', 'materia_grupo_id'])

        # Adding model 'AlumnoTomaClaseEnGrupo'
        db.create_table(u'principal_alumnotomaclaseengrupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
            ('materia_grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.MateriaImpartidaEnGrupo'])),
            ('calificacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['AlumnoTomaClaseEnGrupo'])

        # Adding unique constraint on 'AlumnoTomaClaseEnGrupo', fields ['alumno', 'materia_grupo']
        db.create_unique(u'principal_alumnotomaclaseengrupo', ['alumno_id', 'materia_grupo_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'AlumnoTomaClaseEnGrupo', fields ['alumno', 'materia_grupo']
        db.delete_unique(u'principal_alumnotomaclaseengrupo', ['alumno_id', 'materia_grupo_id'])

        # Removing unique constraint on 'ProfesorDaClaseEnGrupo', fields ['profesor', 'materia_grupo']
        db.delete_unique(u'principal_profesordaclaseengrupo', ['profesor_id', 'materia_grupo_id'])

        # Removing unique constraint on 'ProfesorImparteMateria', fields ['profesor', 'materia']
        db.delete_unique(u'principal_profesorimpartemateria', ['profesor_id', 'materia_id'])

        # Removing unique constraint on 'AlumnoTomaEts', fields ['alumno', 'ets']
        db.delete_unique(u'principal_alumnotomaets', ['alumno_id', 'ets_id'])

        # Removing unique constraint on 'MateriaImpartidaEnLab', fields ['cve_materia_grupo', 'nombre_lab']
        db.delete_unique(u'principal_materiaimpartidaenlab', ['cve_materia_grupo_id', 'nombre_lab_id'])

        # Removing unique constraint on 'MateriaImpartidaEnGrupo', fields ['grupo', 'horario']
        db.delete_unique(u'principal_materiaimpartidaengrupo', ['grupo_id', 'horario_id'])

        # Removing unique constraint on 'MateriaImpartidaEnGrupo', fields ['materia', 'grupo']
        db.delete_unique(u'principal_materiaimpartidaengrupo', ['materia_id', 'grupo_id'])

        # Removing unique constraint on 'Ets', fields ['cve_materia', 'turno']
        db.delete_unique(u'principal_ets', ['cve_materia_id', 'turno'])

        # Removing unique constraint on 'TelefonoUsuario', fields ['cve_usuario', 'tel']
        db.delete_unique(u'principal_telefonousuario', ['cve_usuario_id', 'tel'])

        # Deleting model 'Usuario'
        db.delete_table(u'principal_usuario')

        # Removing M2M table for field groups on 'Usuario'
        db.delete_table(db.shorten_name(u'principal_usuario_groups'))

        # Removing M2M table for field user_permissions on 'Usuario'
        db.delete_table(db.shorten_name(u'principal_usuario_user_permissions'))

        # Deleting model 'Salon'
        db.delete_table(u'principal_salon')

        # Deleting model 'Laboratorio'
        db.delete_table(u'principal_laboratorio')

        # Deleting model 'EmpleadoEscolar'
        db.delete_table(u'principal_empleadoescolar')

        # Deleting model 'Grupo'
        db.delete_table(u'principal_grupo')

        # Deleting model 'Profesor'
        db.delete_table(u'principal_profesor')

        # Deleting model 'Alumno'
        db.delete_table(u'principal_alumno')

        # Deleting model 'TelefonoUsuario'
        db.delete_table(u'principal_telefonousuario')

        # Deleting model 'Depto'
        db.delete_table(u'principal_depto')

        # Deleting model 'Materia'
        db.delete_table(u'principal_materia')

        # Deleting model 'Ets'
        db.delete_table(u'principal_ets')

        # Deleting model 'Horario'
        db.delete_table(u'principal_horario')

        # Deleting model 'MateriaImpartidaEnGrupo'
        db.delete_table(u'principal_materiaimpartidaengrupo')

        # Deleting model 'MateriaImpartidaEnLab'
        db.delete_table(u'principal_materiaimpartidaenlab')

        # Deleting model 'AlumnoTomaEts'
        db.delete_table(u'principal_alumnotomaets')

        # Deleting model 'ProfesorImparteMateria'
        db.delete_table(u'principal_profesorimpartemateria')

        # Deleting model 'ProfesorDaClaseEnGrupo'
        db.delete_table(u'principal_profesordaclaseengrupo')

        # Deleting model 'AlumnoTomaClaseEnGrupo'
        db.delete_table(u'principal_alumnotomaclaseengrupo')


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
            'salario': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
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
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
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
        u'principal.telefonousuario': {
            'Meta': {'ordering': "('cve_usuario',)", 'unique_together': "(('cve_usuario', 'tel'),)", 'object_name': 'TelefonoUsuario'},
            'cve_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Usuario']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'principal.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'administrador': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alergias': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
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
            'enfermedades': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fecha_alta': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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
            'seguro_social_institucion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tipo_sangre': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['principal']
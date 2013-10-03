#encoding:utf-8
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
###########     

from models import Usuario
User = get_user_model()


class CrearusuarioForm(forms.ModelForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Verifica contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = Usuario
        fields = ('nombre','apellidoPaterno','apellidoMaterno','clave',
                'password','clasificacion','curp','nacionalidad','sexo','email_personal','email_institucional','Telefono_Casa','Telefono_Celular','numero_ss',
               'seguroMedico','seguro_social_institucion','estado', 'municipio_o_delegacion', 'calle', 'colonia',
                    'lt','num','mz','cp','alergias','enfermedades','tipo_sangre','foto',
                    'fecha_alta','fecha_nac','administrador', 'activo', 'is_superuser', 'user_permissions')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super(CrearusuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CambiarusuarioForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="<a href='password/'>Cambiar contraseña</a>")
    class Meta:
        model = Usuario
        fields = ('nombre','apellidoPaterno','apellidoMaterno','clave',
                'password','clasificacion','curp','nacionalidad','sexo','email_personal','email_institucional','Telefono_Casa','Telefono_Celular','numero_ss',
                'seguroMedico','seguro_social_institucion','estado', 'municipio_o_delegacion', 'calle', 'colonia',
                    'lt','num','mz','cp','alergias','enfermedades','tipo_sangre','foto','fecha_alta','fecha_nac',
                    'administrador', 'activo', 'is_superuser', 'user_permissions')

    def clean_password(self):
        return self.initial['password']

class InicioForm(forms.Form):
    usuario = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'type':'text', 'autofocus':'True'}), required=True)
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password','type':'password',}), required=True)
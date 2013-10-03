from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, clave, password=None):
        if not clave:
            raise ValueError('Debes elegir una clave')
        user = self.model(clave=clave)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, clave, password):
        user = self.create_user(clave, password)
        user.administrador = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
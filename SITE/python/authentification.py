# Dans votre fichier authentification.py (ou où vous préférez)

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Crée un utilisateur.

        Entrées:
            username (str): Le nom d'utilisateur de l'utilisateur à créer.
            password (str): Le mot de passe de l'utilisateur à créer.
            **extra_fields (dict): Des champs supplémentaires à ajouter à l'utilisateur.

        Sortie:
            user (CustomUser): L'utilisateur créé.
        """
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Crée un compte avec les droits de superutilisateur.

        Entrées:
            username (str): Le nom d'utilisateur du superutilisateur à créer.
            password (str): Le mot de passe du superutilisateur à créer.
            **extra_fields (dict): Des champs supplémentaires à ajouter au superutilisateur.

        Sortie:
            user (CustomUser): Le superutilisateur créé.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

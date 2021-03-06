from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_kwargs):
        if not email:
            raise ValueError('The email is not valid')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)

        if not extra_kwargs.get('is_staff'):
            raise ValueError('SuperUser must be administrator')

        if not extra_kwargs.get('is_superuser'):
            raise ValueError('SuperUser must have is_superuser = True')

        user = self.create_user(email, password, **extra_kwargs)
        return user

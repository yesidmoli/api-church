# from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     PermissionsMixin,
#     BaseUserManager
# )

# class UserManager(BaseUserManager):

#     def create_user(self, email, password , **extra_fields):
#         if not email:
#             raise ValueError('Falta email')
#         user =self.model(email = email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user
    
#     def create_superuser(self, email, password):
#         user = self.create_superuser(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=255)
#     is_staff = models.BooleanField(default =False)
#     is_active = models.BooleanField(default=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
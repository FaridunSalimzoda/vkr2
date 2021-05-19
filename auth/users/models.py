from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Error e-mail')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user =  self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using = self._db)
        return user

class user(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name= 'E-mail',
        max_length= 255,
        unique=True
    )
    is_active = models.BooleanField('Активированная',default=True)
    is_admin = models.BooleanField('Администратор',default=False)
    is_teacher = models.BooleanField('Преподаватель',default=False)
    is_students = models.BooleanField('Студент',default=True)
    name = models.TextField('Имя',max_length=255, default='name')
    last_name = models.TextField('Фамилия',max_length=255, default='lastname')
    patronymic = models.TextField('Отчество',max_length=255, default='patronymic')
    students_groups = models.TextField('Группа',max_length=10, default='group')

    class Meta:
            verbose_name = 'Пользователя'
            verbose_name_plural = 'Пользователи'

    object = UserManager()

    USERNAME_FIELD  = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        self.first_letter = self.email[0]
        super().save()
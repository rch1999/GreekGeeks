from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class Contact(models.Model):
    organization = models.ForeignKey('Organization', models.CASCADE)
    created_by = models.ForeignKey('User', models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    primary_contact_method = models.ForeignKey('ContactMethod', 
                                               models.CASCADE,
                                               related_name='primary_method_for')


class ContactMethod(models.Model):
    medium = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    contact = models.ForeignKey(Contact, models.CASCADE)

class ContactNote(models.Model):
    contact = models.ForeignKey(Contact, models.CASCADE)
    created_by = models.ForeignKey('User', models.CASCADE)
    created = models.DateTimeField()
    body = models.CharField(max_length=1023)
    models.tags = models.ManyToManyField('Tag')


class Tag(models.Model):
    name = models.CharField(max_length=127)


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email adress.')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    first_name = models.CharField('First Name', max_length=100, blank=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True)

    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()


class Notification(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    created = models.DateTimeField('Created At')
    body = models.CharField('Notification Body', max_length=1023)


class Organization(models.Model):
    institution = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=100)
    chapter_name = models.CharField(max_length=100)
    users = models.ManyToManyField(User,
                                   related_name="member_of")
    admin_users = models.ManyToManyField(User,
                                         related_name='admin_of')

    def __str__(self):
        return self.organization_name

class Task(models.Model):
    organization = models.ForeignKey(Organization, 
                                     models.CASCADE,
                                     verbose_name='Task Organization')
    assigner = models.ForeignKey(User, 
                                 models.CASCADE,
                                 verbose_name='Task Assigner',
                                 related_name='has_assigned')
    assignees = models.ManyToManyField(User, 
                                       verbose_name='Task Assignees')
    title = models.CharField('Task Title', max_length=100)
    body = models.CharField('Task Body', max_length=1023)
    due_date = models.DateTimeField(verbose_name='Due Date')


class OrganizationImage(models.Model):
    organization = models.ForeignKey(Organization, models.CASCADE)
    created = models.DateTimeField()
    created_by = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(upload_to='images')
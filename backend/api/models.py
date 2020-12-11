from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
import uuid


class Contact(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    organization = models.ForeignKey('Organization', models.CASCADE)
    created_by = models.ForeignKey('User',
                                   models.SET_NULL,
                                   null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    primary_contact_method = models.ForeignKey('ContactMethod', 
                                               models.SET_NULL,
                                               null=True,
                                               related_name='primary_method_for')
    rank = models.ForeignKey('ContactRank',
                             models.SET_NULL,
                             null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactRank(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    organization = models.ForeignKey('Organization', models.CASCADE)
    name = models.CharField(max_length=4)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactMethod(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    medium = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class ContactNote(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    contact = models.ForeignKey(Contact, models.CASCADE)
    created_by = models.ForeignKey('User', 
                                   models.SET_NULL,
                                   null=True)
    created = models.DateTimeField()
    body = models.CharField(max_length=1023)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return f"{self.contact}/{self.created_by}"


class Tag(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email adress.')
        if not password:
            raise ValueError('Users must have a valid password')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)

        if 'first_name' in kwargs:
            user.first_name = kwargs['first_name']
        if 'last_name' in kwargs:
            user.last_name = kwargs['last_name']

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

    uuid = models.UUIDField(default=uuid.uuid4)

    first_name = models.CharField('First Name', max_length=100, blank=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True)

    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    email_verified = models.BooleanField('Email Verified', default=False)

    def __str__(self):
        return self.email


class Notification(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(User, models.CASCADE)
    created = models.DateTimeField('Created At')
    body = models.CharField('Notification Body', max_length=1023)

    def __str__(self):
        return f"{self.user}/{self.created}"


class Organization(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    institution = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=100)
    chapter_name = models.CharField(max_length=100)
    users = models.ManyToManyField(User,
                                   related_name="member_of")
    admin_users = models.ManyToManyField(User,
                                         related_name='admin_of')

    def __str__(self):
        return self.organization_name


class MembershipRequest(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    organization = models.ForeignKey(Organization, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f"{self.user}/{self.organization}"


class Task(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    organization = models.ForeignKey(Organization,
                                     models.CASCADE,
                                     verbose_name='Task Organization')
    assigner = models.ForeignKey(User,
                                 models.SET_NULL,
                                 null=True,
                                 verbose_name='Task Assigner',
                                 related_name='has_assigned')
    assignees = models.ManyToManyField(User,
                                       verbose_name='Task Assignees')
    title = models.CharField('Task Title', max_length=100)
    body = models.CharField('Task Body', max_length=1023)
    due_date = models.DateTimeField(verbose_name='Due Date')

    def __str__(self):
        return f"{self.organization}/{self.title}"


def organization_image_path(instance, filename):
    return f'images/organization_{instance.organization.uuid}/{filename}'


class OrganizationImage(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    organization = models.ForeignKey(Organization, models.CASCADE)
    created = models.DateTimeField()
    created_by = models.ForeignKey(User,
                                   models.SET_NULL,
                                   null=True)
    image = models.ImageField(upload_to=organization_image_path)

    def __str__(self):
        return f"{self.image}"

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class Contact(models.Model):
    organization = models.ForeignKey('Organization', models.CASCADE)
    created_by = models.ForeignKey('Member', models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_methods = models.ManyToManyField('ContactMethod')
    primary_contact_method = models.ForeignKey('ContactMethod', 
                                               models.CASCADE,
                                               related_name='primary_contact_method')


class ContactMethod(models.Model):
    medium = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class ContactNote(models.Model):
    contact = models.ForeignKey(Contact, models.CASCADE)
    created_by = models.ForeignKey('Member', models.CASCADE)
    created = models.DateTimeField()
    body = models.CharField(max_length=1023)
    models.tags = models.ManyToManyField('Tag')


class Tag(models.Model):
    name = models.CharField(max_length=127)


class MemberManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email adress.')

        member = self.model(
            email=self.normalize_email(email)
        )

        member.set_password(password)
        member.save()

        return member

    def create_superuser(self, email, password, **kwargs):
        member = self.create_user(email, password, **kwargs)

        member.is_admin = True
        member.save()

        return member


class Member(AbstractBaseUser):
    first_name = models.CharField('First Name', max_length=100, blank=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True)

    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = MemberManager()


class Notification(models.Model):
    member = models.ForeignKey(Member, models.CASCADE)
    created = models.DateTimeField('Created At')
    body = models.CharField('Notification Body', max_length=1023)


class Organization(models.Model):
    institution = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=100)
    chapter_name = models.CharField(max_length=100)
    members = models.ManyToManyField(Member)


class Task(models.Model):
    organization = models.ForeignKey(Organization, 
                                     models.CASCADE,
                                     verbose_name='Task Organization')
    assigner = models.ForeignKey(Member, 
                                 models.CASCADE,
                                 verbose_name='Task Assigner')
    assignees = models.ManyToManyField(Member, 
                                       verbose_name='Task Assignees',
                                       related_name='assignees')
    title = models.CharField('Task Title', max_length=100)
    body = models.CharField('Task Body', max_length=1023)
    due_date = models.DateTimeField(verbose_name='Due Date')


class OrganizationImage(models.Model):
    organization = models.ForeignKey(Organization, models.CASCADE)
    created = models.DateTimeField()
    created_by = models.ForeignKey(Member, models.CASCADE)
    image = models.ImageField(upload_to='images')
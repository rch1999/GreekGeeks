from django.contrib import admin
import api.models as models

# Register your models here.
admin.site.register(models.Contact)
admin.site.register(models.ContactMethod)
admin.site.register(models.ContactNote)
admin.site.register(models.Tag)
admin.site.register(models.User)
admin.site.register(models.Notification)
admin.site.register(models.Organization)
admin.site.register(models.Task)
admin.site.register(models.OrganizationImage)
from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Ccustomer)
admin.site.register(models.Subscriber)
admin.site.register(models.CorUser)
admin.site.register(models.UnSubUser)
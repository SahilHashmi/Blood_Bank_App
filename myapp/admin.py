from pyexpat import model
from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Bloodbank)
admin.site.register(models.Donor)
admin.site.register(models.Receiver)
admin.site.register(models.MyUser)
admin.site.register(models.Complaint)

from django.contrib import admin
from . models import User, LocalResident, Organiser
from . import models

# Register your models here.


admin.site.register(User)
admin.site.register(Organiser)
admin.site.register(LocalResident)

admin.site.register(models.Course)
admin.site.register(models.Lecturer)
admin.site.register(models.Article)
admin.site.register(models.Sport)
admin.site.register(models.Event)
admin.site.register(models.Venue)
admin.site.register(models.Schedule)
admin.site.register(models.Enrollment)


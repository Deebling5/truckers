from django.contrib import admin

# Register your models here.
from .models import Job
from .models import Applicant

admin.site.register(Job)
admin.site.register(Applicant)

from django.contrib import admin
from ResumeApp.models import Resume
# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['Name']

admin.site.register(Resume,ResumeAdmin)
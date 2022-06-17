from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(ImportExportActionModelAdmin):
    list_display = ('student_id','name','sex','location','phone_number','total_all')    #displat detail field in local admin

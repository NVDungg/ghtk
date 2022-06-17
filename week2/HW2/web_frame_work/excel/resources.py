from import_export import resources
from .models import Student

class StudentResource(resources.ModelResource):     #use lib django-import-export to take model
    class Meta:
        model = Student

from django.contrib import admin
from.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'company_name', 'age', 'city', 'state', 'zip', 'email', 'web']


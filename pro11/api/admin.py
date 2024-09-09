from django.contrib import admin
from .models import Student,Category,Question,Answer
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact','gender']


class AnswerAdmin(admin.StackedInline):
    model = Answer


class QuetionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Question,QuetionAdmin)
admin.site.register(Answer)
admin.site.register(Category)


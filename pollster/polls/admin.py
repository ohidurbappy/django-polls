from django.contrib import admin
from .models import Question,Choice

admin.AdminSite.site_header="Polls Admin"
admin.AdminSite.site_title="Polls Admin"
admin.AdminSite.index_title="Welcome to Dashboard"
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)